import cv2

img_path = './images/bird.jpg'

img = cv2.imread(img_path, 0)
cv2.imshow('window-name', img)
cv2.waitKey(0)   # Wait infinitely for a keyPress
cv2.destroyAllWindows()
