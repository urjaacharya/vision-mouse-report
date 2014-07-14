def laser_center(self, frame):
    x = y = w = h = 0
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, self.lower_red, self.upper_red)
    res = cv2.bitwise_and(frame, frame, mask= mask)
    thresh = 70
    blur = cv2.medianBlur(mask, 5)
    edges = cv2.Canny(blur, thresh, thresh*2)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, \
        cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        cnt = contours[0]
        cv2.drawContours(frame, contours, -1, (255, 0, 0), -1)
        M = cv2.moments(cnt)         
        try:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
            x, y, w, h = cv2.boundingRect(cnt)          
        except ZeroDivisionError:
            flag = False
    return [x, y, w, h]