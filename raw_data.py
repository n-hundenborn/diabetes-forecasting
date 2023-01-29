# zip files: https://towardsdatascience.com/dont-download-read-datasets-with-url-in-python-8245a5eaa919






import pandas as pd
from io import StringIO, BytesIO, TextIOWrapper
from zipfile import ZipFile
import urllib.request 
import requests


ZIP_URL = "https://www.kaggle.com/datasets/cdc/behavioral-risk-factor-surveillance-system/download?datasetVersionNumber=1"
ZIP_ORDNER = "archive.zip"
CSV_FILE = "2011.csv"


resp = urllib.request.urlopen(ZIP_URL)
# req = requests.get(ZIP_URL)

print(resp)


# reading and storing zip file content
# zipfile = ZipFile(BytesIO(req.content))
zipfile = ZipFile(BytesIO(resp.read()))

# directory = "\raw data"


# with zipfile as zip_ref:
#     zip_ref.extract(CSV_FILE,directory)
# pd.read_csv(directory + CSV_FILE)


# data = TextIOWrapper(zipfile.open(CSV_FILE), encoding = "utf-8")
# print("data:" , data)
# df = pd.read_csv(data)
# print("df:" , df)


# 


# re = urlopen(ZIP_URL)
# files_zip = zipfile.Zipfile(BytesIO(re.read()))

# df = pd.read_csv(FILE)

