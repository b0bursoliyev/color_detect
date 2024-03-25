import cv2
import numpy as np
from util import get_limits

cap = cv2.VideoCapture(0)

while True:
  ret,frame = cap.read()

  cv2.imshow('frame',frame)

  if cv2.waitKey(0) & 0xFF==ord('q'):
    break

cap.release()
cv2.destroyAllWindows()