import numpy as np
import pandas as pd
from ftplib import FTP_TLS
from urllib.request import urlopen
import shutil
import urllib.request as request
from contextlib import closing
import ftplib
import os, datetime, io , csv , re , itertools

def valor_linha(linha):
    cor=[]
    txt=''+ linha+ ' '
    x=[m.start() for m in re.finditer('=', txt)]
    x.append(len(txt)-1)
    valor=''
    peso='0'
    peso1='1'
    if 'STOCK' in txt:
        cor.append(peso1)
    else:
        cor.append(peso)
        
    for i in range(len(x)):
        if (i==len(x)-1):
            break;
        for j in range(x[i],x[i+1]):
            if (txt[j].isdigit()==True or txt[j]=='.'):
                valor+=txt[j]
                if(txt[j+1].isalpha()==True or txt[j+1]==' ' or  txt[j+1]=='\n'):
                    break 
        cor.append(valor)
        valor=''
    return cor
    
    path='C:/Users/valer/OneDrive/Ambiente de Trabalho/estagio/dados'
path1='C:/Users/valer/OneDrive/Ambiente de Trabalho/estagio/raios'
os.listdir(path)
coo=[]
for moldes in os.listdir(path):
    print('#molde',moldes)
    for pecas in os.listdir(path+'/'+moldes):
        print('*peça',pecas)
        coordenadas=[]
        for operacoes in os.listdir(path+'/'+moldes+'/'+pecas):
            print(operacoes)
            if('.txt' not in operacoes):
                linha=''
                coo=[]
                with open(path+'/'+moldes+'/'+pecas+'/'+operacoes) as ft: 

                    linha=''
                    linha_r=''
                    linha_stock=''
                    for line in ft:
                        if (line.lstrip().startswith('%')==False and 'MSG'  not in line):

                            if ('DIAM' in line or 'RAIO TOPO' in line or 'RT' in line or 'DIÂMETRO' in line or 'RAIO' in line or 'FR' in line ) :#or ('DIÂMETRO' in line and 'RT' in line)or ('RAIO' in line and 'RT' in line)
                                linha_r+= line
                                
                
                            if('STOCK' in line):
                                linha_stock+=line
                            linha=linha_r+ " " +linha_stock


                coo=valor_linha(linha)
                split_str=[]
                for t in coo:
                    n=5
                    if len(t)>5:
                        for index in range(0, len(t), n):
                            split_str.append(t[index : index + n])

                    else:
                        split_str.append(t)
                if(split_str[0]=='0' and len(split_str)>4):
                    split_str=split_str[:-2]
                    
                coordenadas.append(split_str)

        print('coordinates done')
        out = list(itertools.chain(*coordenadas))
        

        con_num = []
        for item in out:
            con_num.append(float(item))
        
        print('num',con_num)
        
        ficheiro= open(path1+'/{}.txt'.format(pecas),'w')
        out = csv.writer(ficheiro)
        out.writerows(map(lambda x: [x], con_num))
        ficheiro.close()
    
