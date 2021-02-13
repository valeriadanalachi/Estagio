import numpy as np
import os, csv, itertools, io,re,math, statistics
import pandas as pd 

path_inicial='C:/estagio_dados/modelo3_maiscoord'

###método que evita as coordenadas duplicadas ###
def tratamento(cam):
    
    for r in cam:
        if (r[0]==' =' or r[0]=='' or r[1]==' =' or r[1]=='' or r[2]==' =' or r[2]==''):
            cam.remove(r)
    caminhos1=[]
    if len(cam)>0:
        caminhos1.append(cam[0])
        for u in range(len(cam)):
            if u+1==len(cam):
                break
            else:
                if cam[u+1]!=cam[u]:
                    caminhos1.append(cam[u+1])
        return caminhos1
    else:
        return caminhos1
        
        
        
###função que escreve as coordenadas e chama os outros métodos ###
def coordinates(oper,path1,path2):
    import re, os, csv
    print(path1+'/'+oper)
    caminhos=[]

    mylines = []

    linhasG = []
    x_antigo=0
    y_antigo=0
    z_antigo=0
    semG=True
    with open(path1+'/'+oper) as myfile:
        for linha in myfile:
            mylines.append(linha)

    jump = 0
    #caminhos.append(raios_diametros(oper,path1))
    #save indexes of G01 and G1
    for i in range(len(mylines)):
        if 'G17' not in mylines[i]:       
            if (mylines[i].find('G1')!=-1 or mylines[i].find('G01')!=-1):
                linhasG.append(i)
    if len(linhasG)>0:
        semG=False
        dimen_fin=linhasG[len(linhasG)-1]
        dimen_ini=linhasG[0]

        for n in range(dimen_fin+1,len(mylines) - 1):
            if 'G' in mylines[n]:
                linhasG.append(n)
                break
   

        for i in range(len(linhasG) - 1):

            if (linhasG[i+1] - linhasG[i] > jump):
                for j in range(linhasG[i],linhasG[i+1]):
                    xxx = ""
                    yyy = ""
                    zzz = ""
                    xx=''
                    yy=''
                    zz=''

                    st='GAFCHIR'
                    s='       '
                    var=''.maketrans(st,s)
                    t=mylines[j].translate(var)

                    if 'X' in t:

                        tx=t.translate(''.maketrans('YZ','  '))
                        xxx=re.search('X(.+?) ' , tx)
                        x_antigo=xxx
                        if not xxx:
                            xxx=re.search('X(.+?)\n' , tx)
                            x_antigo=xxx


                    else:
                        xxx=x_antigo

                    if 'Y' in t:
                        ty=t.translate(''.maketrans('XZ','  '))
                        yyy=re.search('Y(.+?) ' , ty)
                        y_antigo=yyy
                        if not yyy:
                            yyy=re.search('Y(.+?)\n' , ty)
                            y_antigo=yyy

                    else:
                        yyy=y_antigo

                    if 'Z' in t:
                        tz=t.translate(''.maketrans('YX','  '))
                        zzz=re.search('Z(.+?) ' , tz)
                        z_antigo=zzz
                        if not zzz:
                            zzz=re.search('Z(.+?)\n' , tz)
                            z_antigo=zzz
                    else:
                        zzz=z_antigo


                    if xxx:
                        xx = str(xxx.group(1))

                    if yyy:
                        yy = str(yyy.group(1))

                    if zzz:
                        zz = str(zzz.group(1))
                    '''else :
                        zz = 0'''
                    if(xx!='' and yy!='' and zz!=''):
                        caminhos.append((xx,yy,zz))
                        #caminhos.append([])
                        #print((xx,yy,zz))
        
        
    if semG==True:
        t=0
        x_antigo1=0
        y_antigo1=0
        z_antigo1=0
        for line in mylines:
            if 'X = AC(' in line or 'Y = AC(' in line or 'Z' in line:


                if 'Z' in line:
                    val_z=''
                    z=line.find('Z')
                    #print(z)
                    for i in range(z,len(line)):
                        if line[i]=='.' or line[i].isdigit() or line[i]=='-':
                            #print(val_Z)
                            val_z+=line[i]
                    z_antigo1=val_z
                else:
                    val_z=z_antigo1



                if 'X' in line:
                    val_x=''
                    x=line.find('X')
                    for i in range(x,len(line)):
                        if line[i]=='Y':
                            break

                        if line[i]=='.' or line[i].isdigit() or line[i]=='-':
                            #print(val_Z)
                            val_x+=line[i]
                    x_antigo1=val_x
                else:
                    val_x=x_antigo1


                if 'Y' in line:
                    val_y=''
                    y=line.find('Y')

                    for i in range(y,len(line)):
                        if line[i]=='Z':
                            break

                        if line[i]=='.' or line[i].isdigit() or line[i]=='-':
                            #print(val_Z)
                            val_y+=line[i]

                    y_antigo1=val_y
                else:
                    val_y=y_antigo1

                if(val_x!='' and val_y!='' and val_z!=''):
                    caminhos.append((val_x,val_y,val_z))
        
    print('*',semG)
    caminho_final=tratamento(caminhos)
    if len(caminho_final)<1:
        print('nao ha caminho')
    
    else:
        with open(path2+'/coord{}.txt'.format(oper),'w') as c:
            csv.writer(c,delimiter=',').writerows(caminho_final)
        return caminho_final
    print(caminho_final[0:5])
#print('coordinates done')


### percorre as diretorias ###
for moldes in os.listdir(path_inicial):
    print('#molde',moldes)
    
    for pecas in os.listdir(path_inicial+'/'+moldes):
        print('*peça',pecas)
        
        for frtr in os.listdir(path_inicial+'/'+moldes+'/'+pecas):
            print('--',frtr)
                        
            if 'Frente' in frtr or 'frente' in frtr or 'FRT' in frtr or 'FRENTE' in frtr or '0' in frtr:
                  for frente in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',frente)  
                        cam=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
                        if frente=='NC': 
                            for operacoes in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr+'/'+frente):
                                coord=coordinates(operacoes,path_inicial+'/'+moldes+'/'+pecas+'/'+frtr+'/'+frente,cam)
                                
                                
            if 'Frente_Mont' in frtr:
                  for frentemont in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',frentemont)  
                        cam=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
                        if frentemont=='NC':
                            for operacoes in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr+'/'+frentemont):
                                coord=coordinates(operacoes,path_inicial+'/'+moldes+'/'+pecas+'/'+frtr+'/'+frentemont,cam)
                                        
                            
            if 'Tras' in frtr or 'tras' in frtr or 'TRS' in frtr or 'TRAS' in frtr: 
                  for tras in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',tras)
                        cam=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
                        if tras=='NC':
                            for operacoes in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr+'/'+tras):
                                coord=coordinates(operacoes,path_inicial+'/'+moldes+'/'+pecas+'/'+frtr+'/'+tras,cam)
                        
                                 
            if 'XP' in frtr or 'xp' in frtr:
                  for xp in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',xp)
                        cam=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
                        if xp=='NC':
                            for operacoes in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr+'/'+xp):
                                coord=coordinates(operacoes,path_inicial+'/'+moldes+'/'+pecas+'/'+frtr+'/'+xp,cam)
                                               
                        
            if 'xn' in frtr or 'XN' in frtr:
                  for xn in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',xn)
                        cam=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
                        if xn=='NC':
                            for operacoes in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr+'/'+xn):
                                coord=coordinates(operacoes,path_inicial+'/'+moldes+'/'+pecas+'/'+frtr+'/'+xn,cam)
                        
                  
            if 'yp' in frtr or 'YP' in frtr:
                  for yp in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',yp)
                        cam=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
                        if yp=='NC':
                            for operacoes in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr+'/'+yp):
                                coord=coordinates(operacoes,path_inicial+'/'+moldes+'/'+pecas+'/'+frtr+'/'+yp,cam)
                      
                      
            if 'yn' in frtr or 'YN' in frtr:
                  for yn in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',yn)
                        cam=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
                        if yn=='NC':
                            for operacoes in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr+'/'+yn):
                                coord=coordinates(operacoes,path_inicial+'/'+moldes+'/'+pecas+'/'+frtr+'/'+yn,cam)
       

            if 'Mont' in frtr:
                  for mont in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',mont)
                        cam=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
                        if mont=='NC':
                            for operacoes in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr+'/'+mont):
                                coord=coordinates(operacoes,path_inicial+'/'+moldes+'/'+pecas+'/'+frtr+'/'+mont,cam)
