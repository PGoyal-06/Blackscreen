import cv2
import numpy as np

cap = cv2.VideoCapture(0)
image = cv2.imread('image.jpg')

while True:
    ret, frame = cap.read()
    
    image = cv2.resize(image,(640,480))
    frame = cv2.resize(frame,(640,480))

    l_black = np.array([30,30,0], dtpye=np.uint8)
    u_black = np.array([104,153,70], dtype=np.uint8)

    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    f = frame - res
    f = np.where(f == 0, image, f)

    cv2.imshow('Real Video', frame)
    cv2.imshow('Masked Video', f)

    if cv2.waitKey(0) == ord('q') or cv2.waitKey(0) == 27:
        break
cap.release()
cv2.destroyAllWindows()