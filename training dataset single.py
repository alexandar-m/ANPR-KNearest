import cv2
import numpy as np
import datetime

start = datetime.datetime.now()

print("Start creating KNearest char samples and responses from font-eu folder!\n")

# ============================================================================

CHARS = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def load_char_images():
    characters = {}
    for char in CHARS:
        print(char)
        char_img = cv2.imread("dataset-single/%s.jpg" % char, 0)
        #print (char_img)
        characters[char] = char_img
    return characters

# ============================================================================

characters = load_char_images()

samples =  np.empty((0,4000))
for char in CHARS:
    char_img = characters[char]
    small_char = cv2.resize(char_img,(50,80))
    sample = small_char.reshape((1,4000))
    samples = np.append(samples,sample,0)

responses = np.array([ord(c) for c in CHARS],np.float32)
responses = responses.reshape((responses.size,1))

np.savetxt('char_samples.data',samples)
np.savetxt('char_responses.data',responses)

end = datetime.datetime.now()
total= end-start
print("\nSpeed: "+(str(total)))

print("\nCreated char_samples.data and char_responses.data!")

# ============================================================================
