import pandas as pd
import os
import random

FOLDER_PATH = "./data/"

GOOGLE_URL = "gs://brfss_datasets/"

files_to_load = [
    "2011.csv",
    "2012.csv",
    "2013.csv",
    "2014.csv",
    "2015.csv"
]


def save_file_from_cloud(file):
    
    if os.path.exists(FOLDER_PATH + file):
        print("You already have this file. No need to download it again.")
        if os.path.exists(FOLDER_PATH + file[:-3] +"pkl"):
            return 0
        else:
            print(f"Reading {file}. This can take some time...")
            df = pd.read_csv(FOLDER_PATH + file)
    else:
        print(f"Downloading {file}. This can take some minutes...")
        df = pd.read_csv(GOOGLE_URL + file)
        print(f"Finished download. Selecting columns.")

    df = df[[
        "DIABETE3",
        "SMOKE100",
        "PREGNANT",
        "_BMI5",
        "SMOKDAY2",
        "CVDSTRK3",
        "PHYSHLTH",
        "SEX",
        "GENHLTH",
        "CVDINFR4",
        "CVDCRHD4",
        "ASTHMA3",
        "STOPSMK2",
        "ALCDAY5",
        "AVEDRNK2",
        "DRNK3GE5",
        "INSULIN",
        "ASATTACK",
        "_TOTINDA",
        "_AGEG5YR",
        "_LTASTH1",
        "_BMI5CAT",
        "_RFBMI5",
        "_RFSMOK3",
        "DRNKANY5",
        "_RFBING5"
    ]]

    file = file[:-3] + "pkl"
    print(f"Writing to {FOLDER_PATH + file}...")
    
    df.to_pickle(FOLDER_PATH + file)
    print(f"File was saved to {FOLDER_PATH + file}.")
    return 1


# fetch and download elements from input list from the google cloud folder
def save_all_files(files=files_to_load):
    print(f"Get a coffee ;) \nDownloading and saving {len(files)} big files will take between {2 * len(files)} and {4 * len(files)} minutes.")
    
    # just in case data folder does not exist, create it
    if not os.path.exists(FOLDER_PATH):
        os.mkdir(FOLDER_PATH)
    
    finished_downloads = 0
    for file in files:
        finished_downloads += save_file_from_cloud(file)
    print(f"You successfully downloaded {finished_downloads} of the {len(files)} files.")


# concats all csv files from the data folder to one dataframe and returns it (using an inner join on the df columns)
def concat_df():
    df_list = []
    
    for file in os.listdir(FOLDER_PATH):
        if not file.endswith(".pkl"):
            continue
        print(f"Reading file: {file}")
        df_list.append(pd.read_pickle(FOLDER_PATH + file))
    
    return pd.concat(df_list, axis=0, ignore_index=True)

# concats all csv files from the data folder to one dataframe and returns it (using an inner join on the df columns)
def concat_sampled_df(sample_size = 10000):
    df_list = []
    
    for file in os.listdir(FOLDER_PATH):
        if not file.endswith(".pkl"):
            continue

        file_path = FOLDER_PATH + file
        n = sum(1 for line in open(file_path)) - 1 #number of records in file (excludes header)
        skip = sorted(random.sample(range(1,n+1),n-sample_size)) #the 0-indexed header will not be included in the skip list

        print(f"Reading file: {file}")
        df_sampled = pd.read_pickle(file_path)
        df_list.append(df_sampled)
    
    return pd.concat(df_list, axis=0, ignore_index=True)