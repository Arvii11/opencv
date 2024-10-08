import cv2

img = cv2.imread('Wayanad.jpg', -1)
img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('Wayanad_2021.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

