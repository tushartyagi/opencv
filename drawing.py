import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# Where to draw, starting point, ending point, BGR color, thickness
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# img, top-left, bottom-right, color, thickness
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# img, center, radius, color, thickness
img = cv2.circle(img, (157, 246), 60, (0, 0, 255), 6)
# There are even ellipsis and polygons, but I am not writing them here
# Showing text in the images:
# Where to write, what to write, bottom left of text,
# font-type, size, color, thickness, line-type
cv2.putText(img, 'This is the end...my friend',
            (100, 217), cv2.FONT_HERSHEY_COMPLEX,
            1, (255, 255, 255), 1, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
