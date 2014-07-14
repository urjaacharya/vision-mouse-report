h, s, v = cv2.split(hsv)
average = np.average(v)
print "average of v", average
if average < 0:
	average = 0
elif average > 255:
	average = 255
if average > AIV_threshold:
	camera.exposure_compensation = camera.exposure_compensation -\
	 (average - AIV_threshold)/10