# import the necessary packages
import cv2
import imutils
from matplotlib import pyplot as plt

image = cv2.imread("tableshot.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edgeMap = imutils.auto_canny(gray, sigma=.33)
# print(edgeMap)
# skeleton = imutils.skeletonize(edgeMap, size=(3, 3))
# print(skeleton)

cv2.imwrite('anything.png', edgeMap)
