
# coding: utf-8

# In[ ]:

import os
from configobj import ConfigObj
from numpy import *

cl_w40=ConfigObj('counts_w40_IM_PG.ini')
folder='cl_w40_mtr/'
root='IMPGw40z03_'

#compute n_s var
n_s=0.9667
hns=array([-0.2,-0.1,0.1,0.2])
nsrange=n_s+hns

for i in range(4):
    if i==0:
        ext='2m'
    elif i==1:
        ext='1m'
    elif i==2:
        ext='1p'
    else:
        ext='2p'
    cl_w40['output_root']=folder+root+'ns_'+ext
    cl_w40['scalar_spectral_index(1)']=str(nsrange[i])
    cl_w40.write()    
    os.system('./camb counts_w40_IM_PG.ini')

cl_w40['output_root']=''
cl_w40['scalar_spectral_index(1)']=str(n_s)
cl_w40.write()


#compute O_b var keping matter content fixed. 
Ob=0.05
hob=array([-0.02,-0.01,0.01,0.02])
Obrange=Ob+hob
Ocdm=0.31-Obrange


for i in range(4):
    if i==0:
        ext='2m'
    elif i==1:
        ext='1m'
    elif i==2:
        ext='1p'
    else:
        ext='2p'
    
    cl_w40['output_root']=folder+root+'Ob_'+ext
    cl_w40['omega_cdm']= str(Ocdm[i])
    cl_w40['omega_baryon']= str(Obrange[i])
    cl_w40.write()    
    os.system('./camb counts_w40_IM_PG.ini')

cl_w40['output_root']=''
cl_w40['omega_cdm']= str(0.31-Ob)
cl_w40['omega_baryon']= str(Ob)
cl_w40.write()  

#delete ini and scalcls
os.system('rm '+folder+'*.ini')
os.system('rm '+folder+'*_scalCls.dat')



