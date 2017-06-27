#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 11:44:22 2017

@author: Quentin
"""

#%%
import os, re, hashlib

def find_duplicates(directory, suffix='.txt'):
    '''
    Returns a list of files with suffix extension in present folder (recursively)
    '''
    home_dir_path = os.path.abspath(directory)
    #print(home_dir_path)
    #file_dir_list = os.listdir(home_dir_path)
    #print(file_dir_list)
    md5_dico = dict()   # Create a dictionary which will have all the files for each checksum
    for dp, dn, fn in os.walk(home_dir_path):
        for f in fn:
            if (re.search(suffix+'$', f) != None):
                #print(os.path.join(dp, f))
                try:
                    tmp_hash = hashlib.md5(open(f,'rb').read()).hexdigest()
                    if tmp_hash in md5_dico:
                        md5_dico[tmp_hash].append(f)
                    else:
                        md5_dico[tmp_hash] = [f]
                except:
                    pass
    #print duplicates
    print("Liste of duplicate files: ")
    for key in md5_dico:
        if len(md5_dico[key])>1:
            print(md5_dico[key])
    
    #return [os.path.join(dp, f) for dp, dn, fn in os.walk(home_dir_path) for f in fn and True]


find_duplicates('/Users/Quentin/Documents/Python', '.*')

#%%
