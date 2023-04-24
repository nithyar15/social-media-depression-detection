import pandas as pd
import numpy as np
import json
import os
from tqdm import tqdm
import logging
from utils import maybe_download_and_extract
from data import DataSet, DataSets
from utils import maybe_download_and_extract, getlink
import requests
import os
import sys
import stat

import wget
import os
from os.path import expanduser
 
def something():    
    myhome = expanduser(r"C:\Users\nithy\CIP Project\input data")
    ### set working dir
    os.chdir(myhome)
 
    url = SOURCE_URL
    print('downloading ...')
    wget.download(url)

os.chmod(r"C:\Users\nithy\CIP Project\input data\data\negative", stat.S_IRWXO )
os.chmod(r"C:\Users\nithy\CIP Project\input data\data\positive", stat.S_IRWXO )

SOURCE_URL = "http://www.mediafire.com/file/33gw4n73pyoa2ea/data.zip/file"
SOURCE_URL1 = "https://www.dropbox.com/s/rd4stk35i80s5hg/data.zip?dl=0"
DATA_DEFAULT_PATH = r"C:\Users\nithy\CIP Project\input data\input.txt"
DATA_DEFAULT_PATH1 = r"C:\Users\nithy\CIP Project\input data\input.txt"
DEFAULT_TEST_SIZE=.25
DEFAULT_SEED=2020

if __name__ == "__main__":
    file_id = 'TAKE ID FROM SHAREABLE LINK'
    destination = 'DESTINATION FILE ON YOUR DISK'
    download_file_from_google_drive(file_id, destination)

def _read_data(data_path):

    # Import data
    tweets=[]
    labels=[]
    data_path = r"C:\Users\nithy\CIP Project\input data"
    labels_path = data_path+'\data\\'
    for cathegory in os.listdir(labels_path):
        data_files=labels_path+cathegory
        files = os.listdir(data_files)
        for file in tqdm(files):
            with open(data_files+'\\'+ file, encoding="utf8", errors="ignore") as json_d:
                tmp = json.load(json_d)
            tweets.append(tmp['text'])
            if cathegory=='negative':
                labels.append(0)
            if cathegory=='positive':
                labels.append(0)
    x, y = np.array(tweets), np.array(labels)
    return x, y


def load_data(data_path=DATA_DEFAULT_PATH1, test_size=DEFAULT_TEST_SIZE, seed=DEFAULT_SEED):

    data_path = os.path.expanduser(data_path)

    x, y = _read_data(data_path)

    data = DataSet(x, y, seed=seed)
    train, test = data.split(split_size=test_size)
    train, validation= train.split(split_size=test_size)
    return DataSets(train,validation,test)
