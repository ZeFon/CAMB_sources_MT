
# coding: utf-8

# In[ ]:

import os
from configobj import ConfigObj
from numpy import *

#variations that affect Pk
pk=ConfigObj('params.ini')

pk['output_root']='pk/fid'
pk.write()

os.system('./camb params.ini')
normdata=loadtxt('pk/fid_transfer_out.dat')
normfid=normdata[0,6]
print(normfid)
savetxt('pk/TkD_fid.dat',c_[normfid,0])

#compute A_s var
A_s=2.142e-9
has=array([0.90,0.95,1.05,1.1])
asrange=A_s*has
normAs=zeros(4)
for i in range(4):
    if i==0:
        ext='2m'
    elif i==1:
        ext='1m'
    elif i==2:
        ext='1p'
    else:
        ext='2p'
    pk['output_root']='pk/As_'+ext
    pk['scalar_amp(1)']=str(asrange[i])
    pk.write()    
    os.system('./camb params.ini')
    #in the folder pk is for As
    normdata=loadtxt('pk/As_'+ext+'_transfer_out.dat')
    normAs[i]=normdata[0,6]

#go back to normal from A_s

pk['output_root']=''
pk['scalar_amp(1)']=str(A_s)
pk.write()

#O_m 
#compute O_m var
Ocdm=0.26
hocdm=array([0.94,0.97,1.03,1.06])
Ocdmrange=Ocdm*hocdm
Ol=1-0.05-Ocdmrange
normOm=zeros(4)

for i in range(4):
    if i==0:
        ext='2m'
    elif i==1:
        ext='1m'
    elif i==2:
        ext='1p'
    else:
        ext='2p'
    #in the main folder pk is for Om
    pk['output_root']='pk/Ocdm_'+ext
    pk['omega_cdm']= str(Ocdmrange[i])
    pk['omega_lambda']= str(Ol[i])
    pk.write()    
    os.system('./camb params.ini')
    #in the folder pk is for As
    normdata=loadtxt('pk/Ocdm_'+ext+'_transfer_out.dat')
    normOm[i]=normdata[0,6]

#go back to normal Ocdm
pk['output_root']=''
pk['omega_cdm']= str(Ocdm)
pk['omega_lambda']= str(1-0.05-Ocdm)
pk.write()

#save norms
savetxt('pk/TkD_As_Ocdm.dat',c_[normAs,normOm],header='A_s     O_cdm')
os.system('rm pk/*.ini')
