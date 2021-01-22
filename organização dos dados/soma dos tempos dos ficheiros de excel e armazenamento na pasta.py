import numpy as np
import pandas as pd
from contextlib import closing
import ftplib
import os, datetime, io , csv , re , itertools


def make_delta(entry):
    try:
        h, m = entry.split(':')
        x= datetime.timedelta(hours=int(h), minutes=int(m))
        return(x)

    except ValueError:
        entry=entry
        
def soma_tempo (paths):
    df = pd.read_csv(paths,encoding='ISO-8859-1')
    data=df.loc[:,['Unnamed: 14']]
    data1=df.loc[:,['Unnamed: 15']]
    #print(df)

    MO= df.loc[:,['Unnamed: 14']].applymap(lambda entry: make_delta(str(entry)))
    #print(MO)
    Maq=df.loc[:,['Unnamed: 15']].applymap(lambda entry: make_delta(str(entry)))
    #print(Maq)

    df['Unnamed: 14']=MO
    df['Unnamed: 15']=Maq
    df['soma1']=df['Unnamed: 14']+df['Unnamed: 15']
    #print(df)
    df1=df.loc[:,['Unnamed: 0','soma1']]

    df1=df1.values.tolist()
    #print(df1)

    #df1.to_csv('p{}.csv'.format())
    return df1
    
path='C:/Users/valer/OneDrive/Ambiente de Trabalho/estagio/dados'
path1='C:/Users/valer/OneDrive/Ambiente de Trabalho/estagio/tempos'
path_excel='C:/Users/valer/OneDrive/Ambiente de Trabalho/estagio/Sensores/Moldes Baby'
os.listdir(path)
coo=[]
for moldes in os.listdir(path_excel):
     if('-' not in moldes):
        for molde_dados in os.listdir(path):
            #print ('moldes daddos',molde_dados)
            if (moldes[4:8]==molde_dados):
                print(moldes)
                dest='C:/Users/valer/OneDrive/Ambiente de Trabalho/estagio/Sensores/Moldes Baby/{}'.format(moldes)
                df = soma_tempo(dest)
                for peca in os.listdir(path+'/'+molde_dados):
                    print(peca)
                    for n in df:
                        val=n[0]
                        val1=n[1]
                        if(val==peca[8:]):
                            print(val)
                            f= open(path1+'/{}-tempo.txt'.format(peca),"w+")
                            f.write(str(n[1]))
