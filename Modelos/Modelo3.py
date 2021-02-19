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


path_inicial='C:/estagio_dados/modelo3_maiscoord'


def dest (d):
    
    try:
        line1=d.split(':')
        horas=int(line1[0])+ int(line1[1])/60  
        return (horas)
    
    except ValueError:
        pass
   
   
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
    
    
def stepz(infz):
    try:
        with open(infz, 'r') as file:
            for i in file:
                val=i
                break
        return val
    except FileNotFoundError:
        pass
        
        
def defin_orient():
    Quart=[]
    for param in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
        #print('----',param)
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
            #print(len(treino))

            for i in df:
                i=i.split(';')
                try:
                    rd=raios_diametros(i[4])[0]
                    temp=dest(i[-4])
                    temp1=dest(i[-3])
                    ae=i[9]
                    rotacao=i[11]
                    avanco=i[12]
                    
                    
                    '''if i[10]=='0.00':
                        #print('steps',i[1],i[10])
                        if '.' in i[1]:
                            v_z=stepz(des+'/'+'compcoord'+i[1].split('.')[0]+'.txt')
                            #print('steps',i[1],v_z)
                        else:
                            v_z=stepz(des+'/'+'compcoord'+i[1]+'.txt')
                    else:
                        v_z=i[10]'''
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
                        #print(j)
                        co=open(des+'/'+j)
                        coord=[]

                        for n in co:
                            if(n!='None\n'):
                                coord.append(float(n))
                        coord1=sum(coord)
                        time=[]
                        #rad=[]
                        
                        tempo=tempos[j[9:].split('.')[0]]
                        tempo2=tempos1[j[9:].split('.')[0]]
                        #print(tempo)
                        try:
                            tempo1=float((list(tempo)[0]))
                        except TypeError:
                            tempo1=float((list(tempo2)[0]))
                            
                        
                        r_d=raios[j[9:].split('.')[0]]
                        r_d1=float((list(r_d)[0].replace(',','.')))
                        #print(r_d1)
                        
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
                        
                        #print(len(treino))
                except KeyError:
                    pass



arr_tempos=[]
for moldes in os.listdir(path_inicial):
    print('#molde',moldes)
    
    for pecas in os.listdir(path_inicial+'/'+moldes):
        #print('*peça',pecas)
        
        for frtr in os.listdir(path_inicial+'/'+moldes+'/'+pecas):
            #print('--',frtr)
                        
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
                
                
treino2=[]
for i in treino:
    if i==None:
        pass
    else:
        treino2.append(i)
print(treino2[0:5])


treino1=[]
for i in range (len(treino2)):
    if treino2[i][6]==0:
        pass
    else:
        treino1.append(treino2[i])



x_train=[]
y_train=[]
X_train=[]
Y_train=[]
dataset=[]
    
for i in range(len(treino1)-valores_teste):
    x_train.append(treino1[i][0])
    x_train.append(treino1[i][1])
    x_train.append(treino1[i][2])
    x_train.append(treino1[i][3])
    x_train.append(treino1[i][4])
    x_train.append(treino1[i][5])

    X_train.append(x_train)
    x_train=[]
    y_train.append(round(treino1[i][6],3))
    Y_train.append(y_train)
    y_train=[]
    
x_test=[]
y_test=[]
X_test=[]
Y_test=[]
for i in range(len(treino1)-valores_teste,len(treino1)):
    x_test.append(treino1[i][0])
    x_test.append(treino1[i][1])
    x_test.append(treino1[i][2])
    x_test.append(treino1[i][3])
    x_test.append(treino1[i][4])
    x_test.append(treino1[i][5])
    X_test.append(x_test)
    x_test=[]
    y_test.append(round(treino1[i][6],3))
    Y_test.append(y_test)
    y_test=[]



Xtrain=np.array(X_train).astype('float32')
print(Xtrain.shape)

Ytrain=np.array(Y_train).reshape(Xtrain.shape[0],).astype('float32')
print(Ytrain.shape)

Xtest=np.array(X_test).astype('float32')
print(Xtest.shape)

Ytest=np.array(Y_test).reshape(Xtest.shape[0],).astype('float32')
print(Ytest.shape)



mean = Xtrain.mean(axis=0)
Xtrain -= mean
std = Xtrain.std(axis=0)
Xtrain /= std
Xtest -= mean
Xtest /= std



def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu',
    input_shape=(Xtrain.shape[1],)))
    model.add(layers.Dense(128, activation='relu'))
    model.add(Dropout(0.2))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='Adam', loss='mse', metrics=['mse'])
    return model



epo=500
tr=[]
te=[]

loss_tr=[]
loss_te=[]

val_loss_tr=[]

epoch=[]
model=build_model()
for i in range (1):

    history=model.fit(Xtrain,Ytrain,batch_size=12,epochs=epo,verbose=1,validation_split=0.2)
    lt=history.history['loss']
    loss_tr.append(lt)
    val_lt=history.history['val_loss']
    val_loss_tr.append(val_lt)
    score=model.evaluate(Xtest,Ytest,verbose=1)
    print(score[1])
    te.append(score[1])
    loss_te.append(score[0])
    
 
 
ep=[]
for i in range(1,epo+1):
    ep.append(i)
 
plt.figure(figsize=(20,10))
plt.plot(ep,loss_tr[0],color='dimgray',label='Erro nos dados de treino')
plt.plot(ep,val_loss_tr[0],color='orangered',label='Erro na validação dos dados de treino')



tr=[]
te=[]
x=0
loss_tr=[]
loss_te=[]

epoch=[]
model=build_model()
for i in range (50):
    x+=20
    epoch.append(x)
    model=build_model()
    history=model.fit(Xtrain,Ytrain,batch_size=12,epochs=x,verbose=1,validation_split=0.2)
    lt=history.history['loss']
    loss_tr.append(lt[len(lt)-1])   
    score=model.evaluate(Xtest,Ytest,verbose=1)
    loss_te.append(score[0])

  
  
plt.plot(epoch,loss_tr,color='dimgray',label='Erro nos dados de treino')
plt.plot(epoch,loss_te,color='darkcyan',label='Erro nos dados de teste')
plt.xlabel('Número de épocas')
plt.ylabel('Erros')
plt.title('Relação entre o número de épocas com os erros')
plt.legend()
plt.show()






