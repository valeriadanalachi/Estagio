import numpy as np
from random import random
import os, csv, itertools, io,re,math, statistics
import pandas as pd 

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from __future__ import print_function
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.optimizers import SGD, Adam, RMSprop
from keras.utils import np_utils
from keras import backend as K
from keras import models
from tensorflow.keras.layers.experimental import preprocessing

import matplotlib.pyplot as plt
import plotly 
import plotly.express as px
import plotly.graph_objs as go
plotly.offline.init_notebook_mode(connected=True)

from sklearn.model_selection import train_test_split

from IPython.display import display
from PIL import Image

from keras.callbacks import EarlyStopping, ModelCheckpoint

#diretoria onde os ficheiros estão guardados
path_inicial='C:/estagio_dados/modelo3_maiscoord'

#método que transforma do formato hh:mm para horas/partes de hora 
def dest (d):
    
    try:
        line1=d.split(':')
        horas=int(line1[0])+ int(line1[1])/60  
        return (horas)
    
    except ValueError:
        pass
      
#método que vai buscar o diâmetro à folha de sequências
def raios_diametros(inf):
    t=''
    raios=[]
    for i in inf:
        if i.isdigit() or i==',' or i=='.':
            t=t+''+i
        if i.isalpha():
            t=t+' '
    t=t.split(' ')
    
    for i in t:
        if i!='':
            raios.append(i)
    return(raios)
  
  
#método que percorre cada orientação da peça

def defin_orient():
    Quart=[]
    for param in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
        des=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
        if param=='zone3.csv':
            df=open(des+'/zone3.csv','r',encoding ="utf8")
            raios={}
            steps={}
            stepse={}
            rot={}
            avan={}
            tempos={}
            tempos1={}

            for i in df:
                i=i.split(';')
                try:
                    rd=raios_diametros(i[4])[0]
                    temp=dest(i[-4])
                    temp1=dest(i[-3])
                    ae=i[9]
                    rotacao=i[11]
                    avanco=i[12]
                    v_z=i[10]   
                        


                    if '.' in i[1]:
                        raios[i[1].split('.')[0]]={rd}
                        steps[i[1].split('.')[0]]={v_z}
                        tempos[i[1].split('.')[0]]={temp}
                        tempos1[i[1].split('.')[0]]={temp1}
                        stepse[i[1].split('.')[0]]={ae}
                        rot[i[1].split('.')[0]]={rotacao}
                        avan[i[1].split('.')[0]]={avanco}
                        
                        
                    else:
                        raios[i[1]]={rd}
                        steps[i[1]]={v_z}
                        tempos[i[1]]={temp}
                        tempos1[i[1]]={temp1}
                        stepse[i[1]]={ae}             
                        rot[i[1]]={rotacao}
                        avan[i[1]]={avanco}
                except IndexError:
                    continue



            for j in os.listdir(des):
                try:
                    if j.startswith('compcoord'):
                        co=open(des+'/'+j)
                        coord=[]

                        for n in co:
                            if(n!='None\n'):
                                coord.append(float(n))
                        coord1=sum(coord)
                        time=[]
                        
                        tempo=tempos[j[9:].split('.')[0]]
                        tempo2=tempos1[j[9:].split('.')[0]]
                        try:
                            tempo1=float((list(tempo)[0]))
                        except TypeError:
                            tempo1=float((list(tempo2)[0]))
                            
                        
                        r_d=raios[j[9:].split('.')[0]]
                        r_d1=float((list(r_d)[0].replace(',','.')))

                        
                        step=steps[j[9:].split('.')[0]]
                        step1=float((list(step)[0]))
                        
                        stepe=stepse[j[9:].split('.')[0]]
                        stepe1=float((list(stepe)[0]))
                        
                        av=avan[j[9:].split('.')[0]]
                        av1=float((list(av)[0]))
                        
                        ro=rot[j[9:].split('.')[0]]
                        ro1=float((list(ro)[0]))
                        
                        
                        arr_tempos.append(tempo1)
                        Quart.append(coord1)
                        Quart.append(r_d1)
                        Quart.append(stepe1)
                        Quart.append(step1)
                        Quart.append(ro1)
                        Quart.append(av1)
                        
                        Quart.append(tempo1)
                        if len(Quart)==7 and Quart!=None:
                            treino.append(Quart)
                        Quart=[]
                        
                except KeyError:
                    pass
            
 #o conjunto de treino será guardado na lista "treino" e o conjunto de teste na lista "testes"

treino=[]
arr_tempos=[]
for moldes in os.listdir(path_inicial):
    
    for pecas in os.listdir(path_inicial+'/'+moldes):
        
        for frtr in os.listdir(path_inicial+'/'+moldes+'/'+pecas):
                        
            if 'Frente' in frtr or 'frente' in frtr or 'FRT' in frtr or 'FRENTE' in frtr or '0' in frtr:
                treino.append(defin_orient())
                
            if 'frentemont' in frtr:
                treino.append(defin_orient())
            
            if 'Tras' in frtr or 'tras' in frtr or 'TRS' in frtr or 'TRAS' in frtr:
                treino.append(defin_orient())
                
            if 'xp' in frtr or 'XP' in frtr:
                treino.append(defin_orient())
                
            if 'yp' in frtr or 'YP' in frtr:
                treino.append(defin_orient())
            
            if 'xn' in frtr or 'xn' in frtr:
                treino.append(defin_orient())
            
            if 'YN' in frtr or 'yn' in frtr:
                treino.append(defin_orient())
                
            if 'Mont' in frtr:
                treino.append(defin_orient())
                
 #retira a lista a None
treino2=[]
for i in treino:
    if i==None:
        pass
    else:
        treino2.append(i)
print(treino2[0:1])    


#retira os tempos a zero para nao enviesar a rede
treino1=[]
for i in range (len(treino2)):
    if treino2[i][6]==0:
        pass
    else:
        treino1.append(treino2[i])
print(treino1[0:1])
 
 
#indica o número de valores a usar para teste
valores_teste=200
  
#cria o conjunto de treino e o conjunto de teste aleatóriamente 
test_dataset, training_dataset = train_test_split(treino1, test_size=len(treino1)-valores_teste, train_size=valores_teste) 

#cria o input de treino e de teste e o target de treino e de teste

x_train=[]
y_train=[]
X_train=[]
Y_train=[]

    
for i in range(len(training_dataset)):
    x_train.append(training_dataset[i][0])
    x_train.append(training_dataset[i][1])
    x_train.append(training_dataset[i][2])
    x_train.append(training_dataset[i][3])
    x_train.append(training_dataset[i][4])
    x_train.append(training_dataset[i][5])

    X_train.append(x_train)
    x_train=[]
    y_train.append(round(training_dataset[i][6],3))
    Y_train.append(y_train)
    y_train=[]
    
x_test=[]
y_test=[]
X_test=[]
Y_test=[]
for i in range(len(test_dataset)):
    x_test.append(test_dataset[i][0])
    x_test.append(test_dataset[i][1])
    x_test.append(test_dataset[i][2])
    x_test.append(test_dataset[i][3])
    x_test.append(test_dataset[i][4])
    x_test.append(test_dataset[i][5])
    X_test.append(x_test)
    x_test=[]
    y_test.append(round(test_dataset[i][6],3))
    Y_test.append(y_test)
    y_test=[]
    
    
Xtrain=np.array(X_train).astype('float32')
print('Dimensão do input do conjunto de treino',Xtrain.shape)

Ytrain=np.array(Y_train).reshape(Xtrain.shape[0],).astype('float32')
print('Dimensão do output do conjunto de treino',Ytrain.shape)

Xtest=np.array(X_test).astype('float32')
print('Dimensão do input do conjunto de teste',Xtest.shape)

Ytest=np.array(Y_test).reshape(Xtest.shape[0],).astype('float32')
print('Dimensão do output do conjunto de teste',Ytest.shape)


#normaliza os dados
mean = Xtrain.mean(axis=0)
Xtrain -= mean
std = Xtrain.std(axis=0)
Xtrain /= std
Xtest -= mean
Xtest /= std


#criação do modelo
def build_model():
    model = models.Sequential()
    model.add(layers.Dense(32, activation='relu',
    input_shape=(Xtrain.shape[1],)))
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model
  
k=3
num_val_samples = len(Xtrain) // k
all_scores = []

#Criação de um modelo até às 500 épocas com o objetivo de ver a partir de 
#que época o valor de mae nos dados usados para validação deixam de melhorar.
num_epochs = 500
all_mae_histories = []
for i in range(k):
    print('processing fold #', i)
    val_data = Xtrain[i * num_val_samples: (i + 1) * num_val_samples]
    val_targets = Ytrain[i * num_val_samples: (i + 1) * num_val_samples]
    
    partial_train_data = np.concatenate(
        [Xtrain[:i * num_val_samples],
        Xtrain[(i + 1) * num_val_samples:]],
        axis=0)
    
    partial_train_targets = np.concatenate(
        [Ytrain[:i * num_val_samples],
        Ytrain[(i + 1) * num_val_samples:]],
        axis=0)
    
    model = build_model()
    history = model.fit(partial_train_data, partial_train_targets,
                        validation_data=(val_data, val_targets),
                        epochs=num_epochs, batch_size=10, verbose=0)
    mae_history = history.history['val_mae']

    all_mae_histories.append(mae_history)
    
#criação do gráfico
average_mae_history = [np.mean([x[i] for x in all_mae_histories]) for i in range(num_epochs)]
plt.figure(figsize=(20,10))
plt.plot(range(1, len(average_mae_history) + 1), average_mae_history, color='darkcyan')
plt.xlabel('Épocas')
plt.ylabel('Validation MAE')
plt.show()

def smooth_curve(points, factor=0.9):
    smoothed_points = []
    for point in points:
        if smoothed_points:
            previous = smoothed_points[-1]
            smoothed_points.append(previous * factor + point * (1 - factor))
        else:
            smoothed_points.append(point)
    return smoothed_points
  
smooth_mae_history = smooth_curve(average_mae_history[10:])
plt.figure(figsize=(20,10))
plt.plot(range(1, len(smooth_mae_history) + 1), smooth_mae_history, color='darkcyan')
plt.xlabel('Épocas')
plt.ylabel('MAE')
plt.show() 

#criação do modelo
model = build_model()

#'es' serivirá para o modelo parar de treinar quando o erro na validação deixar de melhorar
es = EarlyStopping(monitor='val_loss', mode='min',patience=5)

#treino do modelo
model.fit(Xtrain, Ytrain,epochs=200, batch_size=10, verbose=1,validation_split=0.3,callbacks=[es])

#avaliação do modelo
test_mae_score, test_mae_score = model.evaluate(Xtest, Ytest)


#criação do gráfico com as previsões
pred_test=model.predict(Xtest)
previsto_test=[]
real_test=[]
ite=[]
count=0
for i in range(Ytest.shape[0]):
    #print(predictions[i],Ytest[i])
    previsto_test.append(pred_test[i][0])
    real_test.append(Ytest[i])
    ite.append(i)
    if (pred_test[i][0]<=Ytest[i]+ 0.1*Ytest[i]) and (pred_test[i][0]>=Ytest[i]- 0.1*Ytest[i]):
        count+=1 
print('O número de vezes que o valor previsto tem um erro até 10% nos dados de teste é de {}%'.format(round(count/Ytest.shape[0],3)*100))
fig = go.Figure()

fig.add_trace(go.Scatter(x=ite, y=real_test,
                    mode='lines',
                    name='valores reais', marker_color='orangered'))
fig.add_trace(go.Scatter(x=ite,y= previsto_test,
                    mode='lines',
                    name='valores previstos', marker_color='darkcyan'))

fig.show()
