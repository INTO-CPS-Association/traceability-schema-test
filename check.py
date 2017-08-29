#!/usr/bin/env python

import os

print "Initializing submodules..."
os.system("git submodule update --init")
print "Pulling latest schemas..."
os.chdir("intocps-ui")
os.system("git pull origin master")
os.chdir("../")

os.chdir("intocps-ui/scripts")
path='../../tool-output/'
for filename in os.listdir(path):
	os.system("python val_oslc.py --dir " + os.path.join(path,filename))
