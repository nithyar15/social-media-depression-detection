import pandas as pd
import numpy as np
import json
import os
from tqdm import tqdm
from utils import maybe_download_and_extract, getlink

SOURCE_URL = "http://www.mediafire.com/file/xp2jp8ezm3ynpc1/Twitter_Data%25282%2529.zip/file"
DATA_DEFAULT_PATH = r"C:\Users\nithy\CIP Project\input data"
DEFAULT_TEST_SIZE = .25
DEFAULT_SEED = 2020


def load_data(data_path=DATA_DEFAULT_PATH, link=SOURCE_URL, test_size=DEFAULT_TEST_SIZE):
    """
    load data from website and return train, test and validation data
    :param data_path where data will be saved
    :param link to data
    :param test_size

    """
    data_path = os.path.expanduser(data_path)
    # Download files
    #maybe_download_and_extract(getlink(link), data_path)
    # read data
    Twitter_data = pd.read_csv(r"C:\Users\nithy\CIP Project\Social_media_Prediction_depression\Scripts\Twitter_Crawler\ProfileInfos1.csv")
    L = len(Twitter_data)
    
    Twitter_data1 = pd.read_csv(r"C:\Users\nithy\CIP Project\Social_media_Prediction_depression\Scripts\Twitter_Crawler\Profileinfos2.csv")
    L = len(Twitter_data1)

    Twitter_data = Twitter_data.sample(frac=1)
    Twitter_data1 = Twitter_data1.sample(frac=1)
    
    Twitter_data2 = pd.concat([Twitter_data, Twitter_data1], ignore_index=True)
    Twitter_data2 = Twitter_data2.sample(frac=1)
    
    train, val, test = np.split(Twitter_data2, [ int(L * (1 - test_size) * (1 - test_size)), int(L * (1 - test_size)) ])
    return train, val, test


def get_username_profile(username, data_path=DATA_DEFAULT_PATH):
    """
    load user's profile for a given username
    :param data_path where data is saved
    :param username 

    """
    timelines = os.listdir(r"C:\Users\nithy\CIP Project\Social_media_Prediction_depression\Scripts\Twitter_Crawler\Timelines")
    clean_usernames = [s.strip('.csv') for s in timelines]
    
    for i in range(len(clean_usernames)):
        #print(clean_usernames[i])
        if clean_usernames[i] == username:
            #print("lucky")
            timeline = pd.read_csv(r"C:\Users\nithy\CIP Project\Social_media_Prediction_depression\Scripts\Twitter_Crawler\Timelines\\" + username + '.csv', index_col=0)
            #print(timeline.head())
            return timeline, 1
     
    df1 = pd.DataFrame()
    return (df1, 0)
