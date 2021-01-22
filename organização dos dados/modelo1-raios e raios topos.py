import numpy as np
import pandas as pd
import os, datetime, io , csv , re , itertools
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import numpy as np

path='C:/Users/valer/OneDrive/Ambiente de Trabalho/estagio/raios'
path1='C:/Users/valer/OneDrive/Ambiente de Trabalho/estagio/tempos'

def dest (d):
    for line in d:
        line=line.split(' ')
        line1=line[2].split(':')
        horas=int(line[0])*24 +int(line1[0])+ int(line1[1])/60  
        return (horas)
        
 treino=[]
for peca in os.listdir(path):
    #print(peca)
    for temp in os.listdir(path1):
        #print(temp)
        if(temp==peca[:-4]+'-tempo.txt'):
            #print(peca,temp)
            coor=[]
            ficheiro_peca=open(path+'/'+peca)
            for t in ficheiro_peca:
                if not t=='\n':
                    t=float(t)
                    coor.append(t)
            time=[]
            treino.append(coor)
            ficheiro_tempo=open(path1+'/'+temp)
            data=dest(ficheiro_tempo)
            time.append(data)
            treino.append(time)
            
treino_arr=np.array(treino,dtype=object).reshape(15,2)
print(treino_arr)

dim=[]
for k in treino_arr:
    dim.append(len(k[0]))
print(dim)
max_dim=max(dim)
print(max_dim)

treino1=[]
for l in treino_arr:
    treino1.append(l[0])
    while(len(l[0])!= max_dim):
        l[0].append(0)
    treino1.append(l[1])
treino1=np.array(treino1,dtype=object)
treino1.reshape(15,2)

treino1=treino1.reshape(15,2)
x_treino=[]
y_treino=[]
for i in range(treino1.shape[0]):
    x_treino.append(treino1[i,0])
    y_treino.append(treino1[i,1])
print(x_treino)
print(y_treino)

x_treino=np.array(x_treino)
x_treino=x_treino.astype(np.float)
y_treino=np.array(y_treino)
y_treino=y_treino.astype(np.float)

x_treino=tf.keras.utils.normalize(x_treino,axis=1)

model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(40,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(40,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(500,activation=tf.nn.softmax))
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(x_treino,y_treino,epochs=20)

