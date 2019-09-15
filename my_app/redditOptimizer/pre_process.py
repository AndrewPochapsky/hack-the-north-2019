import re
import spacy
import html
import pickle
from torch import Tensor, LongTensor
import os.path
#simple preprocess (lower case, remove weird symbols)
UNK = 'xxxunk'
BOS = 'xxxbos'
EOS = 'xxxeos'
def get_corpus(df):
    corpus = ''
    for i in range(len(df.index)):
        corpus += BOS + ' ' + df.iloc[i, -1] + ' ' + df.iloc[i, -2] + ' ' + EOS
    return corpus
def to_lower(t):
    return t.lower()
def sub_br(t):
    "Replaces the <br /> by \n"
    re_br = re.compile(r'<\s*br\s*/?>', re.IGNORECASE)
    return re_br.sub(" ", t)
def sub_lb(t):
    "Replaces the <br /> by \n"
    re_br = re.compile(r'<\s*lb\s*/?>', re.IGNORECASE)
    return re_br.sub(" ", t)
def sub_nl(t):
    t.replace('\n', ' ')
    return t
def spec_add_spaces(t):
    "Add spaces around / and #"
    return re.sub(r'([/#])', r' \1 ', t)
def rm_useless_spaces(t):
    "Remove multiple spaces"
    return re.sub(' {2,}', ' ', t)
def fixup_text(x):
    "Various messy things we've seen in documents"
    re1 = re.compile(r'  +')
    x = x.replace('#39;', "'").replace('amp;', '&').replace('#146;', "'").replace(
        'nbsp;', ' ').replace('#36;', '$').replace('\\n', "\n").replace('quot;', "'").replace(
        '<br />', " ").replace('\\"', '"').replace(' @.@ ', '.').replace(
        ' @-@ ', '-').replace('\\', ' \\ ')
    return re1.sub(' ', html.unescape(x))
#tokenize
def tokenize(corpus, vocab=None):
    tokenizer = spacy.blank("en").tokenizer
    doc = tokenizer(corpus)
    tokens = []
    for token in doc:
        if(token.text.strip() != ""):
            if(vocab != None and token.text not in vocab):
                tokens.append('xxxunk')
            else:
                tokens.append(token.text)
    return tokens
#generate vocab(REMEMBER TOKENS(eos, bos, pad, unk))
TITLE_START = 'xxxts'
TITLE_END = 'xxxte'
def prepare_input(title, body):
    title_tokens = tokenize(title)
    body_tokens = tokenize(body)
    scriptpath = os.path.dirname(__file__)
    vocab_path = os.path.join(scriptpath, 'my_vocab.pkl')
    vocab = None
    with open(vocab_path, 'rb') as f:
        vocab = pickle.load(f)
    title_tokens = [TITLE_START] + title_tokens + [TITLE_END]
    body_tokens = ['xxxbos'] + body_tokens + ['xxxeos']
    #numericalize
    title_nums = []
    for t in title_tokens:
        if(t in vocab):
            title_nums.append(vocab[t])
        else:
            title_nums.append(vocab['xxxunk'])

    body_nums = []
    for t in body_tokens:
        if(t in vocab):
            body_nums.append(vocab[t])
        else:
            body_nums.append(vocab['xxxunk'])
    input_lst = title_nums + body_nums
    return LongTensor(input_lst).unsqueeze(0)
