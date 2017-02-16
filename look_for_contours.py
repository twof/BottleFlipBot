# author:    Adrian Rosebrock
# website:   http://www.pyimagesearch.com

# USAGE
# BE SURE TO INSTALL 'imutils' PRIOR TO EXECUTING THIS COMMAND
# python sorting_contours.py

# import the necessary packages
from imutils import contours
import imutils
import cv2
from matplotlib import pyplot as plt

# load the shapes image clone it, convert it to grayscale, and
# detect edges in the image
image = cv2.imread("cleartableshot.jpg")
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = imutils.auto_canny(gray)

# find contours in the edge map using OpenCV 2.4.X
if imutils.is_cv2():
    print("which")
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)

# find contours in the edge map using OpenCV 3
elif imutils.is_cv3():
    print(cv2.findContours(edged.copy(), cv2.RETR_TREE,
                           cv2.CHAIN_APPROX_SIMPLE)[1])
    (img, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                                      cv2.CHAIN_APPROX_SIMPLE)
    cv2.imwrite('anything.png', img)

# # loop over the (unsorted) contours and label them
# # print(cnts)
# for (i, c) in enumerate(cnts):
#     orig = contours.label_contour(orig, c, i, color=(240, 0, 159))
#
# # loop over the sorting methods
# for method in ("top-to-bottom"):
#     # sort the contours
#     (cnts, boundingBoxes) = contours.sort_contours(cnts, method=method)
#     clone = image.copy()
#
#     # loop over the sorted contours and label them
#     for (i, c) in enumerate(cnts):
#         sortedImage = contours.label_contour(clone, c, i, color=(240, 0, 159))
#
#     # show the sorted contour image
#     cv2.imwrite('anything.png', sortedImage)
