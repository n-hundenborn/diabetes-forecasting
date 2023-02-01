import pandas as pd
import os

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
    df.to_csv(file_path)
    print(f"File was saved to {file_path}.")
    return 1


def save_all_files(files=files_to_load):
    print(f"Get a coffee ;) \nDownloading and saving {len(files)} big files will take at least {2 * len(files)} minutes.")
    
    # just in case data folder does not exist, create it
    if not os.path.exists(FOLDER_PATH):
        os.mkdir(FOLDER_PATH)
    
    finished_downloads = 0
    for file in files:
        finished_downloads += save_file_from_cloud(file)
    print(f"You successfully downloaded {finished_downloads} of the {len(files)} files.")
