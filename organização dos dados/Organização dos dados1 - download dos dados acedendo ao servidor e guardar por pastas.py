import os, sys
import ftplib
from ftplib import FTP, error_perm

directories=[]

def walk_dir(f, dirpath):
    original_dir = f.pwd()
    try:
        f.cwd(dirpath)
    except error_perm:
        return # ignore non-directores and ones we cannot enter

    if dirpath.find('-')!=-1:
        peca = (dirpath.split('/')[3])
        molde=(dirpath.split('/')[2])
        if (dirpath.find('NC')!=-1):
            files_names=[]
            files_names=f.nlst(dirpath)
            if (molde not in directories):
                directories.append(molde)
                os.mkdir('C:/Users/valer/OneDrive/Ambiente de Trabalho/estagio/dados/{}'.format(molde))
            if (peca not in directories):
                directories.append(peca)
                os.mkdir('C:/Users/valer/OneDrive/Ambiente de Trabalho/estagio/dados/{}'.format(molde+'/'+peca))
            for file in files_names:
                local_fn = os.path.join('C:/Users/valer/OneDrive/Ambiente de Trabalho/estagio/dados/{}'.format(molde+'/'+peca), os.path.basename(file))
                local_file = open (local_fn, "wb")
                f.retrbinary("RETR " + file, local_file.write)
                local_file.close()
                
    names = f.nlst()
    
    for name in names: 
        print(name)
        walk_dir(f, dirpath + '/' + name)
        
        
           
    f.cwd(original_dir)  # return to cwd of our caller

f = ftplib.FTP('ftp.iberomoldes.pt')
f.login('edi001' , 'edi#01')
walk_dir(f, '/')
f.quit()






# In[ ]:




