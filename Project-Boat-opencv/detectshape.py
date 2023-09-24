import cv2
import imutils

def change_threshold(value):
    global threshold
    threshold = value

def detection(p):
    period = cv2.arcLength(p,True)
    approx = cv2.approxPolyDP( p, 0.04 * period, True )
    if len(approx) == 4:
        (x,y,w,h) = cv2.boundingRect(approx)
        return "square"
    else:
        return "circle"

ratio = 4.285714285714286 # 카메라 사용 전 설정할 것.
threshold = 60


cam_index = 1  
cam = cv2.VideoCapture(cam_index)
cv2.namedWindow('target')
cv2.createTrackbar('threshold', 'target', threshold, 255, change_threshold)

while cv2.waitKey(1) < 0:
    ret, frame = cam.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, threshold, 255, cv2.THRESH_BINARY)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        M = cv2.moments(c)
        try:
            cX = int((M["m10"] / M["m00"]) * ratio)
            cY = int((M["m01"] / M["m00"]) * ratio)
            c = c.astype("float")
            c *= ratio
            c = c.astype("int")
            shape = detection(c)
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
            cv2.putText(frame, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            cv2.imshow("target", frame)
        except ZeroDivisionError:
            pass

cv2.destroyAllWindows()
