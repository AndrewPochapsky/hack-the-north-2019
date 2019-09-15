import pandas as pd
import torch
from torch import nn, Tensor, tensor, LongTensor
from torch.utils.data import DataLoader, TensorDataset, Dataset
import torch.nn.functional as F
from pathlib import Path
import spacy
import pickle
import random
import math
import re
import numpy as np
import html
from collections import Counter
from spacy.symbols import ORTH
from concurrent.futures import ProcessPoolExecutor
from ast import literal_eval
import warnings
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
import os.path

import importlib
# predict = importlib.import_module('predict')
# pre_process = importlib.import_module('pre_process')
from . import predict
from . import pre_process

def get_subreddits(title, body):
    input_tensor = pre_process.prepare_input(title, body)
    model = predict.get_model()
    model.eval()
    pred = model(input_tensor)

    scriptpath = os.path.dirname(__file__)
    category_encoder_path = os.path.join(scriptpath, 'category_encoder.pkl')
    category_encoder = None
    with open(category_encoder_path, 'rb') as f:
        category_encoder = pickle.load(f)
    reverse_cat_encoder = get_reverse_cat_encoder(category_encoder)
    return get_top_5_subreddits(pred, reverse_cat_encoder)



def get_top_5_subreddits(pred, reverse_enc):
    pred = pred.squeeze(0)
    res = []
    for i in range(5):
        s = torch.argmax(pred)
        s = s.item()
        pred[s] = 0
        res.append(reverse_enc[s])
    return res

def get_reverse_cat_encoder(category_encoder):
    res = dict()
    for cat in category_encoder:
        res[category_encoder[cat]] = cat
    return res
