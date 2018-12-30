#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 14:26:44 2017

用于删除 dropbox 同步后的冲突文件
ref:
remove file
https://stackoverflow.com/questions/6996603/delete-a-file-or-folder
@author: haikunhuang
"""
import os
import shutil
print ("Scan...: ")
count = 0
for root, dirs, files in os.walk("D:\\Dropbox\\vr_research\\AmbientProject\\AmbientPaper\\Webpage_UIST_Full\\soundDatabase", topdown=False):
    for name in files:
    # for name in dirs:
        if "mp3" in name:
            count +=1
            print(os.path.join(root, name))
            # remove file
            os.remove(os.path.join(root, name))
            # remove a folder
            #shutil.rmtree(os.path.join(root, name))
print ("count: ", count)
