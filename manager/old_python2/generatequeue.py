#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import urllib2  # the lib that handles the url stuff
import textwrap

def genq():
    last_time_file = open("last_time.txt", "r")
    last_time = int(last_time_file.readline())
    last_time_file.close()
    print("Last_time.txt read and closed")

    data = urllib2.urlopen('https://wlconf.000webhostapp.com/7RaZUP6RCVfEdkmxEH6y.log') # it's a file like object and works just like a file
    print("Online queue retrieved")

    for line in data: # files are iterable
        orig_line = line
        line = line[:500]
        words = line.split()
        if (int(words[0]) > last_time):
            header_size = len(words[0] + words[1] + words[2] + words[3]) + 4
            print("Reading " + words[0])
            text = line[header_size:]
            last_time = int(words[0])
            img = Image.new('RGB', (600, 600), color = (237, 237, 237))
            fnt = ImageFont.truetype('./fonts/Inconsolata/Inconsolata-Regular.ttf', 40)
            print("\tFont found")
            d = ImageDraw.Draw(img)
            text = textwrap.fill(text, width=29)
            d.text((10, 10), words[2] + " " + words[3] + "\n" + text, font=fnt, fill=(28, 26, 27))
            img.save("./queue/img/" + str(last_time) + ".jpg")
            print("\tImg saved")
            caption_file = open("./queue/cap/" + str(last_time) + ".txt", "w")
            caption_file.write(orig_line[header_size:])
            caption_file.close()
            print("\tCaption saved")
            
    data.close()

    last_time_file = open("last_time.txt", "w")
    last_time_file.write(str(last_time))
    last_time_file.close()