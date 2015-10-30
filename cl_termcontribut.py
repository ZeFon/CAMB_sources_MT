
# coding: utf-8

# In[ ]:

import os
from configobj import ConfigObj
from numpy import *

#variations that affect Pk
inifile=ConfigObj('w3_IM_PG_testterms.ini')
folder='test_contribution/'
terms=['counts_density','counts_redshift','DoRedshiftLensing','counts_radial','counts_timedelay','counts_ISW','counts_velocity','counts_potential']

for i in range(len(terms)):
    inifile['output_root']=folder+terms[i]+'_'
    inifile[terms[i]]='T'
    inifile.write()    
    os.system('./camb w3_IM_PG_testterms.ini.ini')
    for j in range(len(terms)-i-1):
        inifile['output_root']=folder+terms[i]+'_'+terms[j+i+1]+'_'
        inifile[terms[j+i+1]]='T'
        inifile.write()    
        os.system('./camb w3_IM_PG_testterms.ini.ini')
        inifile[terms[j+i+1]]='F'
        inifile.write()
    inifile[terms[i]]='F'
    inifile.write()
os.system('rm '+folder+'*_scalCls.dat')