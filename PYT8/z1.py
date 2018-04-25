#!/usr/bin/env python

import subprocess
    
try:
     out1 = subprocess.check_call(["g++ test.cpp -o test1"],shell=True)
except subprocess.CalledProcessError as ex:
    print(ex)
    
try:
     out2 = subprocess.check_call(["./test1"],shell=True)
except subprocess.CalledProcessError as ex:
    print(ex)
