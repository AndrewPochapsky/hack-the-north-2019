import torch
import torch.nn.functional as F
from torch import nn, Tensor, tensor
import warnings
from pathlib import Path
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
import pickle
import importlib
import os.path
awd_lstm = importlib.import_module('awd_lstm')



class Pooling(nn.Module):
    def forward(self, input):
        raw_outputs, outputs, mask = input
        output = outputs[-1]
        lengths = output.size(1) - mask.long().sum(dim=1)
        avg_pool = output.masked_fill(mask[:, :, None], 0).sum(dim=1)
        avg_pool.div_(lengths.type(avg_pool.dtype)[:, None])
        max_pool = output.masked_fill(
            mask[:, :, None], -float('inf')).max(dim=1)[0]
        # Concat pooling.
        x = torch.cat([output[torch.arange(0, output.size(0)),
                              lengths-1], max_pool, avg_pool], 1)
        return output, x


def bn_drop_lin(n_in, n_out, bn=True, p=0., actn=None):
    layers = [nn.BatchNorm1d(n_in)] if bn else []
    if p != 0:
        layers.append(nn.Dropout(p))
    layers.append(nn.Linear(n_in, n_out))
    if actn is not None:
        layers.append(actn)
    return layers


class PoolingLinearClassifier(nn.Module):
    "Create a linear classifier with pooling."

    def __init__(self, layers, drops):
        super().__init__()
        mod_layers = []
        activs = [nn.ReLU(inplace=True)] * (len(layers) - 2) + [None]
        for n_in, n_out, p, actn in zip(layers[:-1], layers[1:], drops, activs):
            mod_layers += bn_drop_lin(n_in, n_out, p=p, actn=actn)
        self.layers = nn.Sequential(*mod_layers)

    def forward(self, input):
        raw_outputs, outputs, mask = input
        output = outputs[-1]
        lengths = output.size(1) - mask.long().sum(dim=1)
        avg_pool = output.masked_fill(mask[:, :, None], 0).sum(dim=1)
        avg_pool.div_(lengths.type(avg_pool.dtype)[:, None])
        max_pool = output.masked_fill(
            mask[:, :, None], -float('inf')).max(dim=1)[0]
        # Concat pooling.
        x = torch.cat([output[torch.arange(0, output.size(0)),
                              lengths-1], max_pool, avg_pool], 1)
        x = self.layers(x)
        return x


def pad_tensor(t, bs, val=0.):
    if t.size(0) < bs:
        return torch.cat([t, val + t.new_zeros(bs-t.size(0), *t.shape[1:])])
    return t


class SentenceEncoder(nn.Module):
    def __init__(self, module, bptt, pad_idx=0):
        super().__init__()
        self.bptt, self.module, self.pad_idx = bptt, module, pad_idx

    def concat(self, arrs, bs):
        return [torch.cat([pad_tensor(l[si], bs) for l in arrs], dim=1) for si in range(len(arrs[0]))]

    def forward(self, input):
        bs, sl = input.size()
        self.module.bs = bs
        self.module.reset()
        raw_outputs, outputs, masks = [], [], []
        for i in range(0, sl, self.bptt):
            r, o, m = self.module(input[:, i: min(i+self.bptt, sl)])
            masks.append(pad_tensor(m, bs, 1))
            raw_outputs.append(r)
            outputs.append(o)
        return self.concat(raw_outputs, bs), self.concat(outputs, bs), torch.cat(masks, dim=1)


def get_text_classifier(vocab_sz, emb_sz, n_hid, n_layers, n_out, pad_token, bptt, output_p=0.4, hidden_p=0.2,
                        input_p=0.6, embed_p=0.1, weight_p=0.5, layers=None, drops=None):
    "To create a full AWD-LSTM"
    rnn_enc = awd_lstm.AWD_LSTM1(vocab_sz, emb_sz, n_hid=n_hid, n_layers=n_layers, pad_token=pad_token,
                        hidden_p=hidden_p, input_p=input_p, embed_p=embed_p, weight_p=weight_p)
    enc = SentenceEncoder(rnn_enc, bptt)
    if layers is None:
        layers = [50]
    if drops is None:
        drops = [0.1] * len(layers)
    layers = [3 * emb_sz] + layers + [n_out]
    drops = [output_p] + drops
    return SequentialRNN(enc, PoolingLinearClassifier(layers, drops))


class SequentialRNN(nn.Sequential):
    "A sequential module that passes the reset call to its children."

    def reset(self):
        for c in self.children():
            if hasattr(c, 'reset'):
                c.reset()

def get_model():
    emb_sz = 300
    nh = 300
    nl = 2
    bptt = 70
    dps = tensor([0.4, 0.3, 0.4, 0.05, 0.5]) * 0.25
    vocab = None
    scriptpath = os.path.dirname(__file__)
    vocab_filename = os.path.join(scriptpath, 'my_vocab.pkl')
    category_filename = os.path.join(scriptpath, 'category_encoder.pkl')
    classifier_filename = os.path.join(scriptpath, 'classifier_3.pt')

    with open(vocab_filename, 'rb') as f:
        vocab = pickle.load(f)
    category_encoder = None
    with open(category_filename, 'rb') as f:
        category_encoder = pickle.load(f)
    model = get_text_classifier(len(vocab), emb_sz, nh, nl, len(category_encoder), vocab['xxxpad'], bptt, *dps)

    model.load_state_dict(torch.load(classifier_filename, map_location='cpu'))
    return model
