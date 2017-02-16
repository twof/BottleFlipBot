# import the necessary packages
import numpy as np
import cv2
import imutils

image = cv2.imread("screen.jpg")
#print(image)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()

# find and draw the keypoints
kp = fast.detect(image, None)

max=kp[-1].pt
for i in kp:
	if i.pt[1]>400 and i.pt[1]<max[1]:
		max=i.pt

print(max)

img2 = image


cv2.drawKeypoints(image, kp, color=(255,0,0), outImage=img2)

cv2.circle(img2, (int(max[0]), int(max[1])), 32, (255,128,0), -1)

# Print all default params
#print("Threshold: ", fast.getInt('threshold'))
#print("nonmaxSuppression: ", fast.getBool('nonmaxSuppression'))
#print("neighborhood: ", fast.getInt('type'))
#print("Total Keypoints with nonmaxSuppression: ", len(kp))

cv2.imwrite('fast_true.png',img2)

# Disable nonmaxSuppression
#fast.setBool('nonmaxSuppression',0)
#kp = fast.detect(img,None)

#print("Total Keypoints without nonmaxSuppression: ", len(kp))

#img3 = cv2.drawKeypoints(img, kp, color=(255,0,0))

#cv2.imwrite('fast_false.png',img3)
