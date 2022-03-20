import cv2
import numpy as np

image = cv2.imread("./miau.png")
height, width, channels = image.shape
num_rows, num_cols = image.shape[:2]


"""
Resize
"""
two_factor_resize = cv2.resize(image, (int(width * 2), int(height * 2)))
half_factor_resize = cv2.resize(image, (int(width * 0.5), int(height * 0.5)))

# cv2.imshow('Image / 2', half_factor_resize)
# cv2.imshow('Image 2x', two_factor_resize)

"""
Translation
"""
translation_matrix = np.float32([
	[1, 0, 100],
	[0, 1, 50]
])

shifted = cv2.warpAffine(image, translation_matrix, (num_cols, num_rows))

# cv2.imshow('Translation', shifted)

"""
Rotation
"""
(center_x, center_y) = (width // 2, height // 2)

rotation_matrix = cv2.getRotationMatrix2D((center_x, center_y), 45, 1.0)
rotated = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow("Rotated by 45 Degrees", rotated)

"""
How affine transformation works?
"""
cv2.waitKey(0)
