#!/usr/bin/env python

import subprocess
import os

with open(os.devnull,'w') as devnull:
    out1 = subprocess.call(["ech Hello World!"], stderr = devnull,shell=True)
    
try:
     out2 = subprocess.check_call(["ech Hello World!"],shell=True)
except subprocess.CalledProcessError as ex:
    print(ex)
