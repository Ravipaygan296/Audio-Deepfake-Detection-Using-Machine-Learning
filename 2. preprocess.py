# Script for feature extraction

import librosa
import numpy as np
import os
import pickle

def extract_features(audio_file):
    audio, sr = librosa.load(audio_file, sr=16000)
    mfccs = librosa.feature.mfcc(y=audio, sr=16000, n_mfcc=13)
    return np.mean(mfccs, axis=1)

def process_data(data_path):
    features, labels = [], []
    for label in os.listdir(data_path):
        label_path = os.path.join(data_path, label)
        for file in os.listdir(label_path):
            file_path = os.path.join(label_path, file)
            features.append(extract_features(file_path))
            labels.append(label)
    return np.array(features), np.array(labels)

data_path = "./data/asvspoof"
features, labels = process_data(data_path)

# Save processed data
with open("./data/features.pkl", "wb") as f:
    pickle.dump((features, labels), f)
