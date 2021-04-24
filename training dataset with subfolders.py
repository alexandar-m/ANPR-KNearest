import cv2
import numpy as np
import os

CHARS = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# ============================================================================

imgs = []
characters = {}

for char in CHARS:
    for file in os.listdir("dataset/"+char+"/"):
        full=os.path.join("dataset/"+char+'/', file)
        char_img = cv2.imread(full)
        #print(full)
        imgs.append(char)
        char_img = cv2.imread(full)
        #cv2.imshow("char_img",char_img)
        characters[char] = char_img
        #characters.append(char_img)

# ============================================================================

print("Start creating KNearest char samples and responses from font-eu folder!\n")

samples =  np.empty((0,4000))
for char in imgs:
    #print (char)
    char_img = characters[char]
    char_img = cv2.cvtColor(char_img, cv2.COLOR_BGR2GRAY)
    small_char = cv2.resize(char_img,(50,80))
    sample = small_char.reshape((1,4000))
    samples = np.append(samples,sample,0)


responses = np.array([ord(char) for char in imgs],np.float32)
responses = responses.reshape((responses.size,1))

np.savetxt('char_samples.data',samples)
np.savetxt('char_responses.data',responses)

print("Created char_samples.data and char_responses.data!")

# ============================================================================
