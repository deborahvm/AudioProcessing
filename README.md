# AudioProcessing
## Classificação de Eventos Sonoros
Esse projeto foca no processamento de sinais de áudios e na extração de características dos mesmos através de uma Rede Neural Convolucional, utilizando o Keras como frontend e o TensorFlow como backend. 

A captura, análise e caracterização automáticas dos sons urbanos são utilizadas na redução da poluição sonora, computação sensível ao contexto e vigilância. Tais aplicações podem melhorar aspectos essenciais da vida urbana, incluindo saúde, mercado imobiliário, segurança e educação. Nesse âmbito, o conjunto de dados utilizado é uma base pública chamada [UrbanSound8K](https://urbansounddataset.weebly.com/urbansound8k.html). Essa base conta com 8732 áudios com duração inferior ou igual a 4 segundos rotulados em 10 classes distintas: ar condicionado, buzina de carro, crianças brincando, latido de cachorro, furadeira, motor de veículo, tiro, britadeira, sirene e música de rua. Com exceção das classes crianças brincando e tiros, todas as outras classes foram selecionadas devido a alta frequência em que aparecem no serviço de reclamações de ruído urbano 311 da cidade de Nova York. 

## Passos importantes 
A metodologia proposta para a classificação de eventos sonoros conta com cinco etapas: 
1. Aquisição de dados, consiste na obtenção dos sinais de áudio obtidos através de base de dados pública;  
2. Pré-processamento, onde os dados serão uniformizados,aumentados e representados em diferentes domínios que serão empregados na etapa 3; O pré-processamento, subdivide-se em 3 passos: (1) aumento dos dados decorrente da aplicação de alterações no conjunto de amostras de treinamento para fins de balanceamento e aumento do número de amostras (scripts: urbansound8k_jams_generator.py e urbansound8k_augmentation.py); (2) uniformização do sinal de áudio, aplicação de reamostragem e quantização dos áudios de treino e teste para garantir homogeneidade e qualidade do sinal de entrada (script: urbansound8k_resample.py); (3) geração da representação do sinal de áudio, que servirá de entrada para etapas de extração de características (script: urbansound8k_spectrogram.py).  
3*. Extração de Características, nesta etapa temos o aprendizado de características por meio de uma CNN é treinada com espectrogramas dos áudios a fim de extrair características relevantes da representação do sinal e gerar um descritor. De posse do descritor, é possível aplicá-lo diretamente na etapa 4; 
4*. Classificação, onde o classificador que será responsável por associar cada áudio a uma classe de evento sonoro. 
5*. Validação, que será utilizada para avaliar se o descritor gerado pode se utilizado pelo método de classificação para detectar as classes de eventos sonoros de maneira acurada.

* estão presentes no notebook: urbansound8k_cnn.ipynb

## Dependências

Segue a lista de bibliotecas necessárias para a execução da metodologia:

[JAMS](https://pypi.org/project/jams/)

  ```pip install jams ```

[LibROSA](https://librosa.github.io/librosa/feature.html)

   ```pip install librosa ```
   
[MUDA](https://muda.readthedocs.io/en/latest/)
 
  ```pip install muda ```
  
[SoX](http://sox.sourceforge.net/)
 
  ```sudo apt install sox```
 
[TensorFlow](https://www.tensorflow.org/)
  
   ```pip install --upgrade pip ```
   ```pip install tensorflow ```
   
[Keras](https://keras.io/)
  
  ```sudo pip install keras```
   
 
  

  


