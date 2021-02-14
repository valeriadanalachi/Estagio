### método que retira transforma o tempo em horas e partes de hora ###
def dest (d):
    try:
        line1=d.split(':')
        horas=int(line1[0])+ int(line1[1])/60  
        return (horas)
    
    except ValueError:
        pass
 
 ### método que retira as informações sobre as dimensoes da peça ###
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
   
 ### método que usa as medias das profundidades quando a profundidade no ficheiro é 0 ###
   def stepz(infz):
    try:
        with open(infz, 'r') as file:
            for i in file:
                val=i
                break
        return val
    except FileNotFoundError:
    
 ### criação do input ###
 
 valores_teste=70
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
    y_train.append(round(treino1[i][6],4))
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
    y_test.append(round(treino1[i][6],4))
    Y_test.append(y_test)
    y_test=[]
    
print(Y_train)

      pass
    
### método que cria as associações entre o ficheiro com os ficheiros zone e cria os dados de input ###
def defin_orient():
    Quart=[]
    for param in os.listdir(path_inicial+'/'+moldes+'/'+pecas+'/'+frtr):
        #print('----',param)
        des=path_inicial+'/'+moldes+'/'+pecas+'/'+frtr
        if param=='zone3.csv':
            df=open(des+'/zone3.csv','r',encoding ="utf8")
            raios={}
            steps={}
            tempos={}
            tempos1={}
            #print(len(treino))

            for i in df:
                i=i.split(';')
                try:
                    rd=raios_diametros(i[4])[0]
                    temp=dest(i[-4])
                    temp1=dest(i[-3])

                    if i[10]=='0.00':
                        #print('steps',i[1],i[10])
                        if '.' in i[1]:
                            v_z=stepz(des+'/'+'compcoord'+i[1].split('.')[0]+'.txt')
                            #print('steps',i[1],v_z)
                        else:
                            v_z=stepz(des+'/'+'compcoord'+i[1]+'.txt')
                    else:
                        v_z=i[10]


                    if '.' in i[1]:
                        raios[i[1].split('.')[0]]={rd}
                        steps[i[1].split('.')[0]]={v_z}
                        tempos[i[1].split('.')[0]]={temp}
                        tempos1[i[1].split('.')[0]]={temp1}
                    else:
                        raios[i[1]]={rd}
                        steps[i[1]]={v_z}
                        tempos[i[1]]={temp}
                        tempos1[i[1]]={temp1}

                except IndexError:
                    continue



            for j in os.listdir(des):
                try:
                    if j.startswith('compcoord'):
                        print(j)
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
                        
                        arr_tempos.append(tempo1)
                        Quart.append(coord1)
                        Quart.append(r_d1)
                        Quart.append(step1)
                        Quart.append(tempo1)
                        if len(Quart)==4 and Quart!=None:
                            treino.append(Quart)
                        Quart=[]
                        
                        print(len(treino))
                except KeyError:
                    pass
                
  ### pecorre as diretorias ###
  treino=[]
arr_tempos=[]
for moldes in os.listdir(path_inicial):
    print('#molde',moldes)
    
    for pecas in os.listdir(path_inicial+'/'+moldes):
        print('*peça',pecas)
        
        for frtr in os.listdir(path_inicial+'/'+moldes+'/'+pecas):
            print('--',frtr)
                        
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
                
 ###guardar apenas os inputs que não têm 'None' ###
 treino1=[]
for i in treino:
    if i==None:
        pass
    else:
        treino1.append(i)
print(treino1)   


### colocar na dimensão certa e dividir por treino/teste e caracteristica/target###
Xtrain=np.array(X_train).astype('float32')
print(Xtrain.shape)

Ytrain=np.array(Y_train).reshape(Xtrain.shape[0],).astype('float32')
print(Ytrain.shape)

Xtest=np.array(X_test).astype('float32')
print(Xtest.shape)

Ytest=np.array(Y_test).reshape(Xtest.shape[0],).astype('float32')
print(Ytest.shape)
