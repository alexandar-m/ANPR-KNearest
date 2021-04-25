import cv2
import imutils
import numpy as np
import datetime

start = datetime.datetime.now()

# ============================================================================

def reduce_colors(img, n):
    Z = img.reshape((-1,3))

    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = n
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    print("reduce_colors")

    return res2 

# ============================================================================

def clean_image(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    resized_img = gray_img
    #resized_img = cv2.resize(gray_img,None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)
    #resized_img = cv2.resize(gray_img,(500,100), interpolation=cv2.INTER_LINEAR)

    resized_img = cv2.GaussianBlur(resized_img,(5,5),0)
    cv2.imwrite('temp/1-licence_plate_large.png', resized_img)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(3,3))
    licence_plate_clahe = clahe.apply(resized_img)
    cv2.imwrite('temp/2-licence_plate_clahe.png', licence_plate_clahe)
    
    equalized_img = cv2.equalizeHist(licence_plate_clahe)
    cv2.imwrite('temp/3-licence_plate_equ.png', equalized_img)

    reduced = cv2.cvtColor(reduce_colors(cv2.cvtColor(equalized_img, cv2.COLOR_GRAY2BGR), 8), cv2.COLOR_BGR2GRAY)
    cv2.imwrite('temp/4-licence_plate_red.png', reduced)

    ret, mask = cv2.threshold(reduced, 64, 255, cv2.THRESH_BINARY)
    cv2.imwrite('temp/5-licence_plate_mask.png', mask) 

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    mask = cv2.erode(mask, kernel, iterations = 1)
    mask = cv2.dilate(mask,kernel,iterations = 1)
    cv2.imwrite('temp/6-licence_plate_mask2.png', mask)
    print("clean_image")

    return mask

# ============================================================================

def extract_characters(img):
    bw_image = cv2.bitwise_not(img)
    #contours = cv2.findContours(bw_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[1]
    contours = cv2.findContours(bw_image.copy(),cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)

    char_mask = np.zeros_like(img)
    #cv2.imshow("bw_image",bw_image)
    
    bounding_boxes = []
    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)
        ar = float (w) / float(h)
        area = w * h
        center = (x + w/2, y + h/2)

        if h>50 and w<100:
        #if ar<1:
        #if (area > 5000) and (area < 50000):
            #x,y,w,h = x-1, y+1, w+2, h+2
            bounding_boxes.append((center, (x,y,w,h)))
            cv2.rectangle(char_mask,(x,y),(x+w,y+h),255,-1)


    cv2.imwrite('temp/7-licence_plate_mask3.png', char_mask)

    clean = cv2.bitwise_not(cv2.bitwise_and(char_mask, char_mask, mask = bw_image))

    bounding_boxes = sorted(bounding_boxes, key=lambda item: item[0][0])  
    charNo=0
    characters = []
    whiteh=80
    whitew=50
    for center, bbox in bounding_boxes:
        x,y,w,h = bbox
        if h>80:
            h=80
        if w>50:
            w=50            
        yoff = round((whiteh-h)/2)
        xoff = round((whitew-w)/2)
        char_image = clean[y:y+h,x:x+w]
        cv2.imshow("clean",clean)
        #cv2.imshow("char_image",char_image)
        white = np.zeros((whiteh,whitew), dtype=np.uint8)
        white = 255*np.ones_like(white)
        #cv2.imshow("white",white)
        #white = char_image[y:y+h,x:x+w]
        #white[0:h, 0:w] = char_image
        white[yoff:yoff+h, xoff:xoff+w] = char_image
        cv2.rectangle(white, pt1=(0,0), pt2=(whitew,whiteh), color=(255,255,255), thickness=5)
        #cv2.imshow("white",white)
        char_image = cv2.resize(char_image,(50,80),interpolation=cv2.INTER_LINEAR)
        #cv2.imshow("char_image"'+str(charNo)+',char_image)
        cv2.imwrite(("plate-contours/"+str(charNo)+".jpg"),white)
        characters.append((bbox, white))
        charNo += 1

    print("extract_characters")

    return clean, characters


def highlight_characters(img, chars):
    output_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    for bbox, char_img in chars:
        x,y,w,h = bbox
        #cv2.rectangle(output_img,(x,y),(x+w,y+h),255,1)

    print("highlight_characters")

    return output_img

# ============================================================================    

print("start")
img = cv2.imread("plates/bih.png")
img = cv2.resize(img,(520,110), interpolation=cv2.INTER_LINEAR)
cv2.imshow("img",img)

img = clean_image(img)
clean_img, chars = extract_characters(img)

output_img = highlight_characters(clean_img, chars)
cv2.imwrite('temp/8-licence_plate_output_img.jpg', output_img)

samples = np.loadtxt('char_samples.data',np.float32)
responses = np.loadtxt('char_responses.data',np.float32)
responses = responses.reshape((responses.size,1))

model = cv2.ml.KNearest_create()
model.train(samples, cv2.ml.ROW_SAMPLE, responses)

plate_chars = ""


for bbox, char_img in chars:

    small_img = cv2.resize(char_img,(50,80))
    #bbox = cv2.resize(bbox,(50,80))
    small_img = char_img.reshape((1,4000))
    small_img = np.float32(small_img)

    retval, results, neigh_resp, dists = model.findNearest(small_img, k=1)
    results = results.astype(int)
    #print (results)
    plate_chars += str(chr((results[0][0])))


end = datetime.datetime.now()
total= end-start
print("\nSpeed: "+(str(total)))
print("Licence plate: %s" % plate_chars)
