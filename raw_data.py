import pandas as pd
import os
import random

FOLDER_PATH = "./data/"

GOOGLE_URL = "gs://brfss_datasets/"

files_to_load = [
    "2015_formats.json",
    "2011.csv",
    "2012.csv",
    "2013.csv",
    "2014.csv",
    "2015.csv"
]


def save_file_from_cloud(file):
    file_path = FOLDER_PATH + file
    
    if os.path.exists(file_path):
        print("You already have this file. No need to download it again.")
        return 0
    print(f"Downloading {file}. This can take some minutes...")
    df = pd.read_csv(GOOGLE_URL + file)
    print(f"Finished download. Writing to {file_path}... ")
    df.to_csv(file_path, index=False)
    print(f"File was saved to {file_path}.")
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
        if not file.endswith(".csv"):
            continue
        print(f"Reading file: {file}")
        df_list.append(pd.read_csv(FOLDER_PATH + file, index_col=False))
    
    return pd.concat(df_list, axis=0, ignore_index=True)

# concats all csv files from the data folder to one dataframe and returns it (using an inner join on the df columns)
def concat_sampled_df(sample_size = 10000):
    df_list = []
    
    for file in os.listdir(FOLDER_PATH):
        if not file.endswith(".csv"):
            continue

        file_path = FOLDER_PATH + file
        n = sum(1 for line in open(file_path)) - 1 #number of records in file (excludes header)
        skip = sorted(random.sample(range(1,n+1),n-sample_size)) #the 0-indexed header will not be included in the skip list

        print(f"Reading file: {file}")
        df_sampled = pd.read_csv(file_path, index_col=False, skiprows=skip)
        df_list.append(df_sampled)
    
    return pd.concat(df_list, axis=0, ignore_index=True)