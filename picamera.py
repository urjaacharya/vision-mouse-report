camera = picamera.PiCamera():
camera.resolution = (640, 480)
camera.framerate = 20
camera.start_recording('my_video.h264')
stream = io.BytesIO()
while True:
	camera.capture(stream, format="jpeg", use_video_port = True)
	frame = np.fromstring(stream.getvalue(), dtype=np.uint8)
	frame = cv2.imdecode(frame, 1)
	#this frame can now be used as any OpenCV captured frame