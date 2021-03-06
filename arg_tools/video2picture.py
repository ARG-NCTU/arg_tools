# AUTOGENERATED! DO NOT EDIT! File to edit: 02_video2picture.ipynb (unless otherwise specified).

__all__ = ['gdown_unzip']

# Cell
import gdown
from zipfile import ZipFile
from PIL import Image
import sys
import os
import cv2

def gdown_unzip(id, filename):
    """download a zipfile and unzip it under data directory
    """
    dataset_url = 'https://drive.google.com/u/1/uc?id=' + id
    dataset_name = "data/"+filename

    if not os.path.isdir(dataset_name):
        gdown.download(dataset_url, output = dataset_name + '.zip', quiet=False)
        zip_file = ZipFile( dataset_name + '.zip')
        #zip_file.extractall()
        zip_file.extractall("data/") # depends on how to zip it
        zip_file.close()