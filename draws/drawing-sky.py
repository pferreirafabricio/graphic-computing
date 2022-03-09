import cv2
import numpy as np

width = 400
height = 400

# Colors
blue = (255, 0, 0)
green = (20, 180, 0)
black = (0, 0, 0)
red = (0, 0, 255)

screen = np.ones((400, 400, 3))

# cv2.line(screen, (0, 0), (width, height), blue)
# cv2.line(screen, (int(width / 2), 0), (int(width / 2), height), green, 5)


"""
Exercise 
A mountain, sky, clouds and a building.
The elements should appear in perspective.
"""

def draw_clouds():
    cloud_min_height = 20
    cloud_max_height = 180

    cloud_min_width = 30
    cloud_max_width = 380

    cv2.circle(screen, (cloud_min_width, 60), 20, blue, -1)
    cv2.circle(screen, (cloud_min_width + 20, 70), 20, blue, -1)
    cv2.circle(screen, (cloud_min_width + 25, 40), 20, blue, -1)
    cv2.circle(screen, (cloud_min_width + 40, 50), 20, blue, -1)

    # cv2.line(screen, (cloud_min_width, 60), (cloud_min_width, 80), black, 2)
    # cv2.line(screen, (cloud_min_width, 80), (cloud_min_width + 40, 80), black, 2)
    # cv2.line(screen, (cloud_min_width + 40, 100), (cloud_min_width + 70, 100), black, 2)

def draw_building():
    building_min_height = 40
    building_max_height = 200

    building_min_width = 100
    building_max_width = 380

    cv2.rectangle(screen, (building_min_width, building_max_height), (building_min_width + 40, building_max_height - 50), green, 2)
    cv2.rectangle(screen, (building_min_width + 20, building_max_height - 20), (building_min_width + 30, building_max_height - 30), green, 2)
    cv2.rectangle(screen, (building_min_width + 40, building_max_height), (building_min_width + 70, building_max_height - 80), green, 2)
    cv2.rectangle(screen, (building_min_width + 60, building_max_height - 40), (building_min_width + 50, building_max_height - 50), green, 2)
    cv2.rectangle(screen, (building_min_width + 70, building_max_height), (building_min_width + 100, building_max_height - 30), green, 2)
    cv2.rectangle(screen, (building_min_width + 80, building_max_height - 15), (building_min_width + 90, building_max_height - 25), green, 2)

def draw_mountain():
    mountain_min_height = 40
    mountain_max_height = 200

    mountain_min_width = 240
    mountain_max_width = 380

    points = np.array(
        [
            [mountain_min_width, mountain_max_height],
            [mountain_min_width + 30, mountain_max_height - 40],
            [mountain_min_width + 50, mountain_max_height - 40],
            [mountain_min_width + 70, mountain_max_height - 100],
            [mountain_max_width, mountain_max_height]
        ],
        np.int32
    )
    # points = points.reshape((-1,1,2))
    cv2.polylines(screen, [points], False, red)

# Sky
cv2.line(screen, (0, int(height / 2)), (width, int(height / 2)), black, 2)

# Clouds
draw_clouds()

# Mountain
draw_mountain()

# Building
draw_building()

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(screen, 'Graphics Computing', (int(width / 10), int(height / 2) + 110), font, 1, black, 2, cv2.LINE_AA)

cv2.imshow("Canvas", screen)
cv2.waitKey(0)


