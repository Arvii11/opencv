import cv2

img = cv2.imread('Wayanad_2021.jpg', -1)

face1 = img[270:350, 90:160].copy()
face2 = img[270:350, 350:420].copy()

img[270:350, 350:420] = face1
img[270:350, 90:160] = face2

cv2.imwrite('face_swap.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

