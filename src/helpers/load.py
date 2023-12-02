import argparse
import gzip
import pickle
from tqdm import tqdm
from fractions import Fraction

def str2float(str):
    return float(Fraction(str))

def cleanData(d):
    d['beer/ABV'] = float(d['beer/ABV'])
    d['review/appearance'] = str2float(d['review/appearance'])
    d['review/aroma'] = str2float(d['review/aroma'])
    d['review/palate'] = str2float(d['review/palate'])
    d['review/taste'] = str2float(d['review/taste'])
    d['review/overall'] = str2float(d['review/overall'])
    return d

def loadAndSave(count, path):
    """
    load the dataset and save them in pickle format for later use.
    """
    data = []
    with gzip.open(path, mode='rt') as f:
        for line in tqdm(f):
            if(len(data) == count): break
            d = eval(line)
            if('beer/ABV' in d and d['beer/ABV'] != '-'): data.append(cleanData(d)) 
    with open("data/data.pkl", mode='wb') as f:
        pickle.dump(data, f)

def loadFromPickle(path):
    """
    Load the saved pickle data for speed access
    """
    with open(path, mode='rb') as f:
        data = pickle.load(f)
    return data
    
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", help="Number of data to be loaded")
    parser.add_argument("-p", "--path", help="Path of data")
    args = parser.parse_args()
    loadAndSave(int(args.count), args.path)
