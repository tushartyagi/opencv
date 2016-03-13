import cv2
import os.path

img_path = './images'
img_name = 'bird.jpg'
win_name = 'window-name'

cv2.namedWindow(win_name)
img = cv2.imread(os.path.join(img_path, img_name), 0)  # Grayscaled it
cv2.imshow(win_name, img)
k = cv2.waitKey(0) & 0xFF
# Wait infinitely for a keyPress

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite(os.path.join(img_path, 'saved_image.jpg'), img)
    cv2.destroyAllWindows()
