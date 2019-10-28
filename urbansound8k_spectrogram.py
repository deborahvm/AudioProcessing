'''
Created on Dec 18, 2018
Updated on Mar 15th, 2019

@author: Deborah Magalhaes

@collaborators: Flavio Henrique, Myllena, Jederson e Fatima Sombra 
'''

import pandas as pd 
import numpy as np
import os
import struct
import glob 
import re #regex
from scipy.io import wavfile as wav
import subprocess
import librosa
from scipy import signal
import pickle

#Caminho do conjunto de teste e conjunto de treino
path_database = '/data/deborah/UrbanSound8K/teste/'
audio_format = 'wav'

#Parametros do espectrograma
sr=44100
hop_length=1024
n_fft=2048
window = signal.blackmanharris(2048)
n_mels=100

#Listas que armazenarao os espectrogramas e classe de cada audio
specs = []
labels = []

#Função que normaliza os dados do espectrogram
def normalization(data):
    data = np.log10(10000*data+1)
    data = (data-np.mean(data))/np.std(data)
    return data

def run():

    #Capturando o nome das pastas
    names_folders = glob.glob(path_database + '*')

    for names_ in names_folders: 

        #Capturando o caminho completo do audio
        path_audios = glob.glob(names_ + '/*.' + audio_format) 

        for path_ in path_audios:

           #Captura o nome do audio
            match_obj = re.sub(names_, "", path_)
            match_obj = re.sub(r'/', "", match_obj)
            match_obj2 = re.sub(match_obj, "", path_)

            #Captura o label da classe
            label = int(match_obj.split('-')[1])

            os.chdir(match_obj2)
            #Captura os primeiros 2.3 segundos do audio
            y, sr = librosa.load(match_obj, sr=None,duration=2.3)
            
            #Aplica a transformada STFT
            S = librosa.stft(y, n_fft= n_fft, hop_length= hop_length, window=window)
            S = np.abs(S)

            #Gera o espectrograma com 100 bandas 
            X = librosa.feature.melspectrogram(y=y, sr=sr, S=S, n_mels=n_mels)

            #Aplica a normalizacao dos dados
            log_spectrogram = normalization(X)

            specs.append(log_spectrogram)
            labels.append(label)

    os.chdir(path_database)
    #Salvando as listas em disco na forma de objetos
    with open('log_specs_100_teste.pickle', 'bw') as f:
        pickle.dump(specs, f)

    with open('labels_100_teste.pickle', 'bw') as f:
        pickle.dump(labels, f)
    
run()
