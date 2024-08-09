import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (0, 255, 0), 3)
    img = cv2.line(img, (0, height), (width, 0), (0, 0, 255), 3)
    img = cv2.rectangle(img, (100, 200), (400, 400), (125, 50, 20), 3)
    img = cv2.circle(img, (320, 240), 25, (47, 74, 58), -1)

    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(img, 'Arvii!!!', (10, height - 10), font, 4, (0, 0, 0), 3)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

