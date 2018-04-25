#!/usr/bin/env python

import subprocess

out1 = subprocess.call(["echo Hello World"],shell=True)
out2 = subprocess.check_output(["echo Hello World"],shell=True)

print(out1)
print(out2)
