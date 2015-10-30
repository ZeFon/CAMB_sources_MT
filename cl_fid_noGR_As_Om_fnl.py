
# coding: utf-8

# In[ ]:

import os
from configobj import ConfigObj
from numpy import *

#variations that affect Pk
cl_w40=ConfigObj('counts_w40_IM_PG_noGR.ini')
folder='cl_w40_mtr/'
root='IMPGw40z03_noGR_'

cl_w40['output_root']=folder+root+'fid'
#include which terms to be acounted in the transfer function. 

cl_w40.write()

os.system('./camb counts_w40_IM_PG_noGR.ini')

normdata=loadtxt('pk/TkD_As_Ocdm.dat')

#compute A_s var
A_s=2.142e-9
has=array([0.90,0.95,1.05,1.1])
asrange=A_s*has

for i in range(4):
    if i==0:
        ext='2m'
    elif i==1:
        ext='1m'
    elif i==2:
        ext='1p'
    else:
        ext='2p'
    cl_w40['output_root']=folder+root+'As_'+ext
    cl_w40['scalar_amp(1)']=str(asrange[i])
    cl_w40.write()    
    os.system('./camb counts_w40_IM_PG_noGR.ini')

cl_w40['output_root']=''
cl_w40['scalar_amp(1)']=str(A_s)
cl_w40.write()

#O_m 
#compute O_m var
Ocdm=0.26
hocdm=array([0.94,0.97,1.03,1.06])
Ocdmrange=Ocdm*hocdm
Ol=1-0.05-Ocdmrange


for i in range(4):
    if i==0:
        ext='2m'
    elif i==1:
        ext='1m'
    elif i==2:
        ext='1p'
    else:
        ext='2p'
    
    cl_w40['output_root']=folder+root+'Ocdm_'+ext
    cl_w40['omega_cdm']= str(Ocdmrange[i])
    cl_w40['omega_lambda']= str(Ol[i])
    cl_w40['normtrans']=str(normdata[i,1])
    cl_w40.write()    
    os.system('./camb counts_w40_IM_PG_noGR.ini')

normfid=loadtxt('pk/TkD_fid.dat')
cl_w40['output_root']=''
cl_w40['omega_cdm']= str(Ocdm)
cl_w40['omega_lambda']= str(1-0.05-Ocdm)
cl_w40['normtrans']=str(normfid[0])
cl_w40.write()  

#vary with respect to fnl
fnlrange=array([-2,-1,1,2])

for i in range(4):
    if i==0:
        ext='2m'
    elif i==1:
        ext='1m'
    elif i==2:
        ext='1p'
    else:
        ext='2p'
    cl_w40['output_root']=folder+root+'fnl_'+ext
    cl_w40['fNL']= str(fnlrange[i])
    cl_w40.write()
    os.system('./camb counts_w40_IM_PG_noGR.ini')

cl_w40['output_root']=''
cl_w40['fNL']= str(0)
cl_w40.write()
#save deltas
savetxt(folder+'hCl.dat',c_[0.05*A_s,0.03*Ocdm,1],header='A_s     O_cdm    fnl')

#delete ini and scalcls
os.system('rm '+folder+'*.ini')
os.system('rm '+folder+'*_scalCls.dat')

