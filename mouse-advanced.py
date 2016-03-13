import cv2
import numpy as np

drawing = False
mode = True
ix, iy = -1, -1


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    # We are starting with drawing, so save the coordinates of
    # the place where the mouse was clicked. We need a global
    # variable for this since the event will keep firing.
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    # Either draw a rectangle or a line depending on the mode.
    # The line is drawn by creating a circle by following the
    # mouse path.
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            if mode is True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 2, (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode is True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv2.circle(img, (x, y), 2, (0, 0, 255), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('image', img)
cv2.setMouseCallback('image', draw_circle)

while (True):
    cv2.imshow('image', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('m'):
        mode = not mode
    elif key == 27:
        break

cv2.destroyAllWindows()
