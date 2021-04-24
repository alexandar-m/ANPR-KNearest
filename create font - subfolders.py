# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import string


import cv2
import array
import imutils
import numpy as np

from pathlib import Path

# Settings
W, H = (50, 80)

# Font
font = ImageFont.truetype("FE-FONT.ttf", 60, encoding='utf-8')
fontname="fe"

alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)
print(alphabet_list)

i = 0
while i < len(alphabet_list):
    print(alphabet_list[i])
    image = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(image)
    offset_w, offset_h = font.getoffset(alphabet_list[i])
    w, h = draw.textsize(alphabet_list[i], font=font)
    pos = ((W-w-offset_w)/2, (H-h-offset_h)/2)

    # Draw
    draw.text(pos, alphabet_list[i], "black", font=font)

    # Save png file

    #p = pathlib.Path(alphabet_list[i])
    #p.mkdir(parents=True, exist_ok=True)

    folder = str("dataset/"+alphabet_list[i]+"/")
    print (folder)
    #char = ("font/"+str(alphabet_list[i]))
    Path(str(folder)).mkdir( parents=True, exist_ok=True)
    image.save(str(folder)+alphabet_list[i]+"-"+fontname+".jpg")
    i += 1

number_list=["0","1","2","3","4","5","6","7","8","9"]
print(number_list)
n = 0
while n < len(number_list):
    print(number_list[n])
    image = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(image)
    offset_w, offset_h = font.getoffset(number_list[n])
    w, h = draw.textsize(number_list[n], font=font)
    pos = ((W-w-offset_w)/2, (H-h-offset_h)/2)

    # Draw
    draw.text(pos, number_list[n], "black", font=font)

    # Save png file
    folder = str("dataset/"+number_list[n]+"/")
    Path(str(folder)).mkdir( parents=True, exist_ok=True)
    image.save(str(folder)+number_list[n]+"-"+fontname+".jpg")
    n += 1
