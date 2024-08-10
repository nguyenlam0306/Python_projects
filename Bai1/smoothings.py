import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

#Average
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

#Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

#Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

#Bilaterial -- like delete background
bilaterial = cv.bilateralFilter(img, 5, 15,15)
cv.imshow('Bilaterial', bilaterial)

cv.waitKey(0)