#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
from os import listdir
from os.path import isfile, join
from random import randint
import os
import time
import generatequeue

InstagramAPI = InstagramAPI("[username]", "[redacted]")
InstagramAPI.login()  # login

while True:
    print("Calling genq()")
    generatequeue.genq()
    print("End of genq()")
    
    cap_dir = "./queue/cap/"
    cap_files = [f for f in listdir(cap_dir) if isfile(join(cap_dir, f))]
    print("Cap queue read, ct: " + str(len(cap_files)))
    img_dir = "./queue/img/"
    img_files = [f for f in listdir(img_dir) if isfile(join(img_dir, f))]
    print("Img queue read, ct: " + str(len(img_files)))

    cap_files.sort()
    img_files.sort()

    print(cap_files)
    print(img_files)

    for name in cap_files:
        name = name[:-4]
        
        photo_path = "./queue/img/" + name + ".jpg"
        caption_path = "./queue/cap/" + name + ".txt"
        
        print("Starting upload process for: " + name)
        
        caption_file = open(caption_path)
        caption_text = caption_file.readline()
        caption_file.close()
        print("\tCaption file read")
        
        InstagramAPI.uploadPhoto(photo_path, caption=caption_text)
        print("\tUpload complete")

        os.rename(caption_path, "./pushed/cap/" + name + ".txt")
        os.rename(photo_path, "./pushed/img/" + name + ".jpg")
        print("\tFiles moved to pushed")
        
        print("\tSleeping for 60 +- 15 seconds, break is safe")
        time.sleep(45 + randint(0, 27))
        print("\tSleep almost over")
        time.sleep(3)
        print("\tSleep end")
        

    print("Depleted cap_files")
    print("Done")
    
    print("Sleeping for 10 seconds, break is safe")
    time.sleep(10)
    print("Sleep almost over")
    time.sleep(3)
    print("Sleep end")