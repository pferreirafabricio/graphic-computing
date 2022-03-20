import cv2
import numpy as np
# import matplotlib.pyplot as plt

image = cv2.imread("./coins.png")
height, width, channels = image.shape

greyImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blurring and erasing little details
# kernel = np.ones((5, 5), np.uint8)
# grey = cv2.GaussianBlur(greyImage, (9, 9), 0)
# grey = cv2.morphologyEx(grey, cv2.MORPH_OPEN, kernel)
# grey = cv2.morphologyEx(grey, cv2.MORPH_CLOSE, kernel)

# Thresholding to highlight the more dark areas
# grey = cv2.threshold(grey, 40, 255, cv2.THRESH_BINARY_INV)[1]
# grey = cv2.morphologyEx(grey, cv2.MORPH_CLOSE, kernel)

# canny = cv2.Canny(grey, 100, 200)

circles = cv2.HoughCircles(
    greyImage,
    cv2.HOUGH_GRADIENT,
    dp = 1.05,  # the higher this value, the more sensitive the detector is, and can cause false positives. If it is too low, some circles may not be detected
    minDist = 10,  # the minimum distance between two circles. Unfortunately this function cannot detect concentric circles
    # Second parameter of the inner Canny that the function applies before the method itself, the first parameter is param1/2.
    param1 = 20,
    param2 = 85,
    minRadius = 1,  # Limits to the size of the circles to be detected. These parameters are not required, but if you have an estimate of the sizes of the circles you want to find they can prevent false detections outside this range
    maxRadius = 50
)

print(circles)
print(f'{len(circles[0])} coins were found!')

base_coin = circles[0][0][2]

base_5 = base_coin - (base_coin * 0.22)
base_10 = base_coin - (base_coin * 0.28)
base_25 = base_coin - (base_coin * 0.15)
base_50 = base_coin - (base_coin * 0.21)

total = 0

for index in circles[0, :]:
    current_radio = index[2]
    if current_radio >= base_coin:
        total += 1
    elif current_radio < base_coin and current_radio >= base_25:
        total += 0.25
    elif current_radio < base_25 and current_radio >= base_50:
        total += 0.5
    elif current_radio < base_50 and current_radio >= base_5:
        total += 0.05
    elif current_radio < base_5 and current_radio >= base_10:
        total += 0.1

print(f'Base coin {base_coin * 0.22}')

# Changing the dtype to int
circles = np.uint16(np.around(circles))
copyImage = image.copy()

for index in circles[0, :]:
    # draw the outer circle
    cv2.circle(copyImage, (index[0], index[1]), index[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(copyImage, (index[0], index[1]), 2, (255, 0, 0), 10)


print(f'R${round(total, 2)} estimated value!')

# plt.imshow(copyImage)
# plt.show()

cv2.imshow('a', copyImage)
cv2.waitKey(0)
