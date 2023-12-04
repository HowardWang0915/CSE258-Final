import argparse
import gzip
import pickle
import numpy as np
from tqdm import tqdm
from fractions import Fraction
from collections import defaultdict

style = defaultdict(int)
brewerID = defaultdict(int)
beerID = defaultdict(int)
def str2float(str):
    return float(Fraction(str))

def cleanData(d):
    d['beer/ABV'] = float(d['beer/ABV'])
    d['review/appearance'] = str2float(d['review/appearance'])
    d['review/aroma'] = str2float(d['review/aroma'])
    d['review/palate'] = str2float(d['review/palate'])
    d['review/taste'] = str2float(d['review/taste'])
    d['review/overall'] = str2float(d['review/overall'])
    if d['beer/brewerId'] not in brewerID:
        if len(brewerID) == 0:
            brewerID[d['beer/brewerId']] = 0
        else:
            brewerID[d['beer/brewerId']] = max(brewerID.values()) + 1
    if d['beer/beerId'] not in beerID:
        if len(beerID) == 0:
            beerID[d['beer/beerId']] = 0
        else:
            beerID[d['beer/beerId']] = max(beerID.values()) + 1
    if d['beer/style'] not in style:
        if len(style) == 0:
            style[d['beer/style']] = 0
        else:
            style[d['beer/style']] = max(style.values()) + 1
    # d['beer/brewerId'] = brewerID[d['beer/brewerId']]
    # d['beer/beerId'] = beerID[d['beer/beerId']]
    # d['beer/style'] = style[d['beer/style']]
    return d

def loadAndSave(count, path):
    """
    load the dataset and save them in pickle format for later use.
    """
    data = []
    with gzip.open(path, mode='rt') as f:
        for line in tqdm(f, total=count):
            if(len(data) == count): break
            d = eval(line)
            if('beer/ABV' in d and d['beer/ABV'] != '-'): data.append(cleanData(d))
    # print(max(style.values()))
    # print(max(beerID.values()))
    # print(max(brewerID.values()))
    with open("data/data.pkl", mode='wb') as f:
        pickle.dump(data, f)

def loadFromPickle(path):
    """
    Load the saved pickle data for speed access
    """
    with open(path, mode='rb') as f:
        data = pickle.load(f)
    return data

def load_embeddings(path):
    return np.load(path)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", help="Number of data to be loaded")
    parser.add_argument("-p", "--path", help="Path of data")
    args = parser.parse_args()
    loadAndSave(int(args.count), args.path)
