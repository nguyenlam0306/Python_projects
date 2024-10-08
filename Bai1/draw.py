import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
# blank[200:300, 400:600] = 0,0,255
# cv.imshow('Red', blank)

# 2. Draw the rectangle 
# cv.rectangle(blank, (0,0), (blank.shape[0]//2 , blank.shape[1]//2),(0,255,0), thickness=2)
# # negative number is filled 
# # cv.imshow('Rectangle', blank)

# # 3. Draw a circle 
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=-3)
# cv.imshow('Circle', blank)

# # 4.Draw a line
# cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
# cv.imshow('Line', blank)

# 5. Put the text 
cv.putText(blank, 'Hello world!', (0,255), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
