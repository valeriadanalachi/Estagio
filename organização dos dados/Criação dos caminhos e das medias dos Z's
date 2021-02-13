### método que cria os comprimentos ###
def comp(ponto1, ponto2):
    try:
        ponto1=ponto1.split(',')
        ponto2=ponto2.split(',')
        d=math.sqrt((float(ponto2[0])-float(ponto1[0]))**2+(float(ponto2[1])-float(ponto1[1]))**2+(float(ponto2[2])-float(ponto1[2]))**2)
        return d
    except ValueError:
        pass
        
 ### método que vai criar a média da profundidade ###
 def prof_z(ponto1, ponto2):
    try:
        ponto1=ponto1.split(',')[2][:2]
        ponto2=ponto2.split(',')[2][:2]
        med=abs(float(ponto2)-float(ponto1))
        return med
    except ValueError:
        pass
        
### métodod que abre as coordenadas ja criadas e cria ficheiros com os comprimentos###
def open_coor(path3,orient):
    path4=path3+'/'+orient
    distancia=[]
    c=[]
    r=0
    m=0
    with open(path4,'rt') as mycoor:
        distan=[]
        for linha in mycoor:
            if linha=='\n':
                del linha
            else:
                c.append(linha)
                
        zs=[]
        for w in range(0,len(c)):
            m=m+1
            if m==len(c):
                break
            else:
                prof=prof_z(c[m],c[w])
                #print(prof)
                if isinstance(prof, type(None))==False:
                    zs.append(prof)
        
        '''for j in c:
            try:
                zes=float(j.split(',')[2])
            except ValueError:
                zes=float(j.split(',')[2][:2])
                
            zs.append(zes)'''
        media=statistics.mean(zs)
        print('media',media)
        distan.append(str(media))

        for i in range(0,len(c)):
            r=i+1
            if r==len(c):
                break
            else:
                #print(c[r],c[i])
                dist=comp(c[r],c[i])
                #print(dist,med)
                distan.append(str(dist))
                
            distancia.append(distan)
        #print(distancia[0])
    with open(path3+'/comp{}.txt'.format(orient.partition(".")[0]),'w') as export:
        for i in range(len(distan)):
            export.write(distan[i]+'\n')
            
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
                        
                        if(frente.startswith('coord') and frente.endswith('.txt')):
                            cal_comp=open_coor(cam,frente)
                            
                            
            if 'Frente_Mont' in frtr:
                
                  for frentemont in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',frentemont)  
                        cam=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
                        
                        if(frentemont.startswith('coord') and frentemont.endswith('.txt')):
                            cal_comp=open_coor(cam,frentemont)

                            
                            
            if 'Tras' in frtr or 'tras' in frtr or 'TRS' in frtr or 'TRAS' in frtr:
                
                  for tras in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',tras)
                        cam=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
    
                        if(tras.startswith('coord') and tras.endswith('.txt')):
                            cal_comp=open_coor(cam,tras)
                        
            
            if 'XP' in frtr or 'xp' in frtr:
                
                  for xp in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',xp)
                        cam=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
                        if(xp.startswith('coord') and xp.endswith('.txt')):
                            cal_comp=open_coor(cam,xp)
                        
                        
            if 'xn' in frtr or 'XN' in frtr:
                
                  for xn in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',xn)
                        cam=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
        
                        if(xn.startswith('coord') and xn.endswith('.txt')):
                            cal_comp=open_coor(cam,xn)
                        
            
            if 'yp' in frtr or 'YP' in frtr:
                
                  for yp in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',yp)
                        cam=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
                    
                        if(yp.startswith('coord')and yp.endswith('.txt')):
                            cal_comp=open_coor(cam,yp)
                            
            if 'yn' in frtr or 'YN' in frtr:
                
                  for yn in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',yn)  
                        cam=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
                        
                        if(yn.startswith('coord') and yn.endswith('.txt')):
                            cal_comp=open_coor(cam,yn)
                            
            if 'Mont' in frtr:
                
                  for mont in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
                        print('----',mont)  
                        cam=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
                        
                        if(mont.startswith('coord') and mont.endswith('.txt')):
                            cal_comp=open_coor(cam,mont)
