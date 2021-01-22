import numpy as np
from ftplib import FTP_TLS
from urllib.request import urlopen
import shutil
import urllib.request as request
from contextlib import closing
import ftplib
import os
import io
import csv, itertools

path='C:/Users/valer/OneDrive/Ambiente de Trabalho/estagio/dados'
path2='C:/Users/valer/OneDrive/Ambiente de Trabalho/estagio/coordenadas1'

os.listdir(path)
for moldes in os.listdir(path):
    print('#molde',moldes)
    for pecas in os.listdir(path+'/'+moldes):
        print('*peça',pecas)
        coordenadas=[]
        for operacoes in os.listdir(path+'/'+moldes+'/'+pecas):
            print(operacoes)
            if(operacoes!= 'coordenadas.txt'):
                with open(path+'/'+moldes+'/'+pecas+'/'+operacoes) as ft: 

                    x=0
                    y=0
                    z=0
                    t=0
                    i=0
                    for line in ft:
                        if ('X' in line or 'Y' in line or 'Z' in line):
                            #x=i[i.index('X')+1:i.index('Y')-1]
                            #print("linha{}".format(i),line)

                            try:
                                #print (i.index('Y'))
                                #x=i[i.index('X')+1:i.index('X')+6]
                                x=line[line.index('X')+1:line[line.index('X')+1:].index('.')+
                                       line.index('X')+1] + line[line[line.index('X')+1:].index('.')+
                                       line.index('X')+1:line[line.index('X')+1:].index('.')+line.index('X')+5] 

                                n=0
                                for f in x:
                                    if (f.isalpha()):
                                        x=x[0:n]
                                    n+=1

                                x=x.rstrip('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdesfgijklmnopqrstuvw.)\n) (')     
                            except ValueError:
                                x=x
                                #.rstrip('ABCDEFGHIJKLMNOPQRSTUVWabcdesfgijklmnopqrstuvw\) (')

                            try:
                                y=(line[line.index('Y')+1:line[line.index('Y')+1:].index('.')+
                                       line.index('Y')+1]+line[line[line.index('Y')+1:].index('.')+
                                       line.index('Y')+1:line[line.index('Y')+1:].index('.')+line.index('Y')+5])

                                n=0
                                for f in y:
                                    if (f.isalpha()):
                                        y=y[0:n]
                                    n+=1
                                y=y.rstrip('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdesfgijklmnopqrstuvw.)\n ) (')
                            except ValueError:
                                y=y

                            try:
                                z=(line[line.index('Z')+1:line[line.index('Z')+1:].index('.')+
                                       line.index('Z')+1]+line[line[line.index('Z')+1:].index('.')+
                                       line.index('Z')+1:line[line.index('Z')+1:].index('.')+line.index('Z')+5])
                                n=0
                                for f in z:
                                    if (f.isalpha()):
                                        z=z[0:n]
                                    n+=1
                                z=z.rstrip('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdesfgijklmnopqrstuvw.)\n ) (')
                            except ValueError:
                                z=z
                            coordenadas.insert(t,[(x),(y),(z)])
                            i+=1
                            t=t+1
                    for r in list(coordenadas):
                        if (r[0]==' =' or r[0]=='' or r[1]==' =' or r[1]=='' or r[2]==' =' or r[2]==''):
                            coordenadas.remove(r)

        print(coordenadas)

        out = list(itertools.chain(*coordenadas))
        con_num = []
        for item in out:
            con_num.append(float(item))

        print('num',con_num)
        
        ficheiro= open(path2+'/{}.txt'.format(pecas),'w')
        out = csv.writer(ficheiro)
        out.writerows(map(lambda x: [x], con_num))
        ficheiro.close()
        
        '''with open(path2+'/{}.txt'.format(pecas),'w') as c:
            csv.writer(c,delimiter=',').writerows(coordenadas)
        print('coordinates done')'''
            
        
                        
arr_coordenadas=np.array(coordenadas)
#print(arr_coordenadas)
