import numpy as np
import os, csv, itertools, io,re,math, statistics
import pandas as pd 
from keras.utils import np_utils
from bs4 import BeautifulSoup 

#metodo que irá converter os ficheiros antigos em csv mas separados por ' ; '
def tocsv(pathzone):
    path1 = pathzone+'/zone.htm'
    path2=pathzone+'/zone'
    html = open(path1)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.findAll("table")[0]
    rows = table.findAll("tr")
    #print(rows)
    with open("{}3.csv".format(path2), "wt+", newline="",encoding='utf-8') as f:
        writer = csv.writer(f,delimiter=';',dialect='excel')
        for row in rows:
            csv_row = []
            for cell in row.findAll(["td", "th"]):
                csv_row.append(cell.get_text())
            writer.writerow(csv_row)
            
            
 #caminho onde os ficheiros estão guardados
 path_inicial='C:/estagio_dados/modelo3_maiscoord'
 

#percorre as pastas para encontrar os ficheiros .htm e guarda os novos ficheiros no mesmo sitio com o nome 'zone3.csv'
 for moldes in os.listdir(path_inicial):
    print('#molde',moldes)
  
    for pecas in os.listdir(path_inicial+'/'+moldes):
        print('*peça',pecas)
        
        if 'Imagens' not in pecas or 'imagens' not in pecas:
        
            for frtr in os.listdir(path_inicial+'/'+moldes+'/'+pecas):
                print('--',frtr)
                
                if 'Frente' in frtr or 'frente' in frtr or 'FRT' in frtr or 'FRENTE' in frtr or '0' in frtr:
                      for frente in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',frente)
                        if 'zone.htm'in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                            new_file=tocsv(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr)

                if 'Frente_Mont' in frtr:
                      for frente in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',frente)
                        if 'zone.htm'in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                            new_file=tocsv(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr)


                if 'Tras' in frtr or 'tras' in frtr or 'TRS' in frtr or 'TRAS' in frtr:
                      for tras in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',tras)
                        if 'zone.htm'in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                            new_file=tocsv(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr)

                if 'XP' in frtr or 'xp' in frtr:
                      for xp in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',xp)
                        if 'zone.htm'in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                            new_file=tocsv(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr)

                if 'xn' in frtr or 'XN' in frtr:
                      for xn in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',xn)
                        if 'zone.htm'in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                            new_file=tocsv(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr)

                if 'yp' in frtr or 'YP' in frtr:
                      for yp in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',yp)
                        if 'zone.htm'in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                            new_file=tocsv(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr)

                if 'yn' in frtr or 'YN' in frtr:
                      for yn in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',yn)
                        if 'zone.htm'in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                            new_file=tocsv(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr)

                if 'Mont' in frtr :
                      for mont in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',mont)
                        if 'zone.htm'in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                            new_file=tocsv(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr)
