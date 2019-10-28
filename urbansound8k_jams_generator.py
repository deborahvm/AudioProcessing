'''
Created on Dec 14, 2018
Updated on Out 21, 2019

@author: Deborah Magalhaes

@collaborators: Flavio Henrique, Myllena, Jederson e Fatima Sombra

'''

import glob 
import re #regex
import os
import jams
import librosa

#Caminho dos audios de treinamento (.wav)
path_database = '/data/deborah/UrbanSound8K/audio/'
audio_format = 'wav'
data_source='UrbanSound8K'
name='Deborah'
email='deborah.vm@ufpi.edu.br'

def run():

    #Capturando os nomes das pastas
    names_folders = glob.glob(path_database + '*')

    for names_ in names_folders:
        
        #Capturando o caminho completo dos audios
        path_audios = glob.glob(names_ + '/*.' + audio_format) 

        for path_ in path_audios:

            #Capturando o nome do arquivo de audio (wav) 
            match_obj = re.sub(names_, "", path_)
            audio_name = re.sub(r'/', "", match_obj)

            #Capturando o caminho completo da pasta
            fold_path = re.sub(audio_name, "", path_)

            os.chdir(fold_path)
            #Capturando a duracao do sinal
            y, sr = librosa.load(audio_name, sr=None)
            duration = librosa.get_duration(y=y, sr=sr)

            #Remove os arquivos de audio que possuem duracao inferior a 2.3s
            if duration >= 2.3:          
              
                #Gerando o arquivo de anotacao jam 
                jam = jams.JAMS()

                #Setando os parametros do arquivo de notacao
                jam.file_metadata.duration = duration
                ann = jams.Annotation(namespace='beat', time=0, duration=jam.file_metadata.duration)
                ann.annotation_metadata = jams.AnnotationMetadata(data_source=data_source)
                ann.annotation_metadata = jams.AnnotationMetadata(validation= "")
                ann.annotation_metadata.curator = jams.Curator(name=name, email=email)
                jam.annotations.append(ann)

                #Salvando o arquivo de notacao para cada audio
                jam_name = re.sub(r'\.wav', ".jams", audio_name)
                jam.save(jam_name)

            else:
                os.system('rm ' +path_)
            
run()
