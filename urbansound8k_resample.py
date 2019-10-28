'''
Created on Dec 06, 2018
Updated OUT 20, 2019

@author: Deborah Magalhaes

@collaborators: Flavio Henrique, Myllena, Jederson e Fatima Sombra
'''
import os
import glob 
import re #regex
import subprocess
import librosa

#Caminho dos audios de treino e teste 
path_database = '/data/deborah/UrbanSound8K/audio/'
audio_format = 'wav'

def run():

    #Capturando o nome das pastas
    names_folders = glob.glob(path_database + '*')

    for names_ in names_folders:

        #Capturando o caminho completo do audio
        path_audios = glob.glob(names_ + '/*.' + audio_format)

        for path_ in path_audios:
            
            #Capturando o nome do arquivo de audio (wav) 
            match_obj = re.sub(names_, "", path_)
            match_obj = re.sub(r'/', "", match_obj)
            match_obj4 = re.sub(match_obj, "", path_)
            match_obj5 = re.sub(r'\.wav', "-resample.wav", path_)
            
            #Capturando a duracao do sinal
            y, sr = librosa.load(path_)
            duration = librosa.get_duration(y=y, sr=sr)

            os.chdir(match_obj4)
            #Desconsidera os audios com duracao inferior a 2.3
            if duration >= 2.3:
                #Reamostrando o sinal de audio e alterando a resolucao para 44.1KHz e 16-bits
                os.system('sox ' +path_+ ' -r 44100 -b 16 ' +match_obj5+' rate')
                os.system('rm ' +path_)
            else:
                os.system('rm ' +path_)

            
run()
