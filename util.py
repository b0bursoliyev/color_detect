import numpy as np
import cv2

def get_limits(color):

  temp = np.uint8([[color]])
  hsv = cv2.cvtColor(temp,cv2.COLOR_BGR2HSV)

  low_limit = hsv[0][0][0] - 10, 100, 100
  high_limit = hsv[0][0][0] + 10, 255, 255

  low_limit = np.array(low_limit, dtype=np.uint8)
  high_limit = np.array(high_limit, dtype=np.uint8)

  return low_limit, high_limit
