# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import string

from pathlib import Path

# Settings
W, H = (50, 80)

# Font
font = ImageFont.truetype("fonts/d-din-condensed-bold.ttf", 85, encoding='utf-8')
fontname="ddin"

# Chars
CHARS = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

print("Start creating img chars!\n")

i = 0
while i < len(CHARS):
    print(CHARS[i])
    image = Image.new("L", (W, H), "white")
    draw = ImageDraw.Draw(image)
    offset_w, offset_h = font.getoffset(CHARS[i])
    w, h = draw.textsize(CHARS[i], font=font)
    pos = ((W-w-offset_w)/2, (H-h-offset_h)/2)

    # Draw
    draw.text(pos, CHARS[i], "black", font=font)

    # Save jpg file
    folder = str("dataset/"+CHARS[i]+"/")
    Path(str(folder)).mkdir( parents=True, exist_ok=True)
    image.save(str(folder)+CHARS[i]+"-"+fontname+".jpg")
    i += 1

print("\nAll chars created in dataset folder!")
