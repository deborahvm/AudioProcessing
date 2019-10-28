'''
Created on Dec 14, 2018
Updated on Out 21, 2019 

@author: Deborah Magalhaes

@collaborators: Flavio Henrique, Myllena, Jederson e Fatima Sombra
'''
import muda
import glob 
import re #regex
import os

#Caminho dos dados de treinamento (.wav e .jams)
path_database = '/data/deborah/UrbanSound8K/audio/'
#Caminho dos audios utilizados como ruido
path_backgound_noise = '/data/deborah/UrbanSound8K/background_noise/'
audio_format = 'wav'
files= glob.glob(path_backgound_noise + '/*.' + audio_format)

def run():

    #Captura os nomes das pastas
    names_folders = glob.glob(path_database + '*')

    for names_ in names_folders:

        #Captura o caminho completo do audio
        path_audios = glob.glob(names_ + '/*.' + audio_format) 

        for path_ in path_audios:

            #Captura o nome do audio sem extensao
            audio_name = re.sub(names_, "", path_)
            audio_name = re.sub(r'/', "", audio_name)
            audio_name_wo_ext = re.sub(r'\.wav', "", audio_name)
      
            #Captura o caminho completo no arquivo de anotacao
            jam_path = re.sub(r'\.wav', ".jams", path_)
            
            #Captura o label da classe
            label = audio_name.split('-')[1]

            # A variacao de semitons e maior para as classes 1 e 6 
            if label == '1' or label == '6':
                semitones=[1,1.5,2,2.5,3,3.5]
            else:
                semitones=[1.5,2,2.5,3]

            jam_orig = muda.load_jam_audio(jam_path, path_) 

            #Gerando variacoes no tom
            ps = muda.deformers.PitchShift(n_semitones=semitones)
            output_name_ps_pattern = names_+'/'+audio_name_wo_ext+ '-ps-'

            #O audio modificado e salvo em um novo .wav e as deformacoes aplicadas sao salvas no seu respectivo .jams
            for i, jam_out in enumerate(ps.transform(jam_orig)):
                muda.save(output_name_ps_pattern+str(semitones[i])+'.wav', output_name_ps_pattern+str(semitones[i])+'.jams',jam_out) 

            #Gerando deformacoes de ruido de fundo
            bg = muda.deformers.BackgroundNoise(n_samples=1, files=files, weight_min=0.1, weight_max=0.5)
            output_name_bg_pattern = names_+'/'+audio_name_wo_ext+'-bg-'

            #O audio modificado e salvo em um novo .wav e as deformacoes aplicadas sao salvas no seu respectivo .jams
            for i, jam_out in enumerate(bg.transform(jam_orig)):
                bg_noise_name = files[i].split('/')[5]
                bg_noise_name_w_extension = re.sub(r'\.wav', "", bg_noise_name)
                muda.save(output_name_bg_pattern+bg_noise_name_w_extension+'.wav', output_name_bg_pattern+bg_noise_name_w_extension+'.jams',jam_out)

run()
