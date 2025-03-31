1. download_data.py
# Script to download and extract ASVspoof dataset

import os
import requests
import tarfile

def download_asvspoof():
    url = "https://datashare.ed.ac.uk/download/DS_10283_3336.zip"  # Example dataset link (ensure access)
    dataset_path = "./data/asvspoof_dataset.zip"
    if not os.path.exists(dataset_path):
        print("Downloading ASVspoof dataset...")
        response = requests.get(url, stream=True)
        with open(dataset_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print("Download complete.")
    else:
        print("Dataset already downloaded.")

def extract_dataset():
    dataset_path = "./data/asvspoof_dataset.zip"
    extract_path = "./data/asvspoof"
    if not os.path.exists(extract_path):
        print("Extracting dataset...")
        with tarfile.open(dataset_path, "r:gz") as tar:
            tar.extractall(path=extract_path)
        print("Extraction complete.")
    else:
        print("Dataset already extracted.")

if __name__ == "__main__":
    download_asvspoof()
    extract_dataset()
