import numpy
import cv2

image = cv2.imread("./miau.png")

cv2.imshow('Image window', image)

height, width, channels = image.shape

print("Image dimensions: ")
print(image.shape)

print("===== Accessing chanells =====")
blue, green, red = cv2.split(image)

# cv2.imshow('Red', blue)
# cv2.imshow('Green', green)
# cv2.imshow('Blue', red)

# print("Accessing pixel: ")
# bluePx,greenPx,redPx = image[120,240]

# print('Red: ' + str(redPx))
# print('Green: ' + str(greenPx))
# print('Blue: ' + str(bluePx))

# hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# cv2.imshow('HSV', hsvImage)

# greyImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grey', greyImage)

vertical_start = (int(width / 2), 0)
vertical_end = (int(width / 2), height)

# Draw a diagonal blue line with thickness of 5 px
vertical_line = cv2.line(image, vertical_start, vertical_end, (0, 0, 0), 5)

horizontal_start = (0, int(height / 2))
horizontal_end = (width, int(height / 2))

horizontal_line = cv2.line(vertical_line, horizontal_start, horizontal_end, (0, 0, 0), 5)

cv2.imshow('Lines', horizontal_line)

cv2.waitKey(0)
