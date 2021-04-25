from PIL import Image, ImageDraw, ImageFont
import string
import datetime

start = datetime.datetime.now()

# Settings
W, H = (50, 80)

# Font
font = ImageFont.truetype("fonts/FE-FONT.ttf", 70, encoding='utf-8')

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
    image.save("dataset-single/"+CHARS[i]+".jpg")
    i += 1

end = datetime.datetime.now()
total= end-start
print("\nSpeed: "+(str(total)))

print("\nAll chars created in dataset-single folder!")
