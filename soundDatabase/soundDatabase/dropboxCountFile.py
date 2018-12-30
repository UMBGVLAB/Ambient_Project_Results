#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 587 sound files
"""
Created on Thu Jan 19 14:26:44 2017


@author: haikunhuang
"""
import os
print ("Scan...: ")
count = 0
for root, dirs, files in os.walk("C:\\Users\\Quincy\\Dropbox\\Unity3D\\Ambient\\Ambient_v5\\soundDatabase", topdown=False):
    for name in files:
        if ".mp3" in name:
            count +=1
            print(os.path.join(root, name))
print ("count: ", count)
