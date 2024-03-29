import cv2
from util import get_limits

cap = cv2.VideoCapture(0)
yellow = [0, 255, 255]  # yellow in BGR
low_limit, high_limit = get_limits(yellow)

while True:
    ret, frame = cap.read()

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_image, low_limit, high_limit)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x1, y1, w, h = cv2.boundingRect(contour)
        x2, y2 = x1 + w, y1 + h
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
