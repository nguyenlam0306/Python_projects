import cv2 as cv
import numpy as np

img = cv.imread('../Photos/cats.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)


# Simple thresholding
threhold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('simple Thresh', thresh)

threhold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('simple Thresh Inverse', thresh_inv)

#Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('ADAPTIVE', adaptive_thresh)


cv.waitKey(0)