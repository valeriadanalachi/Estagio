import pandas as pd
import re,os
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.express as px

path='C:/Users/valer/OneDrive/Ambiente de Trabalho/estagio/pasta de testes 4/para os graficos'
path1='C:/Users/valer/OneDrive/Ambiente de Trabalho/estagio/pasta de testes 4/graficos'

x=[]
y=[]
z=[]
raios=[]

w=0
for t in os.listdir(path):
    ficheiro=[]
    w+=1
    r=0
    with open(path+'/'+t) as file:
        print(t)
        for i in file:
            #print(i)
            if r==0:
                i=i.split(',')
                raio=float(''.join(i))
            else:
                if i=='\n':
                    del i
                else:
                    ficheiro.append(float((i.split(',')[0])))
                    ficheiro.append(float((i.split(',')[1])))
                    ficheiro.append(float((i.split(',')[2])))
            r+=1
            
        siz=int((len(ficheiro))/3)
        print(siz)
        ficheiro=np.array(ficheiro).reshape(siz,3)
        dataset = pd.DataFrame({'X': ficheiro[:, 0], 'Y': ficheiro[:, 1],'Z': ficheiro[:, 2]})
        df = dataset

        fig = px.line_3d(df, x='X', y="Y", z="Z")
        
        fig.update_traces(line=dict(color='darkred', width=raio/10))
        fig.write_html(path1+'/{}.html'.format(t))
        fig.show()
        #so para mostrar a primeira
        break
