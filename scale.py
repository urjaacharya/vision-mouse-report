width = capture.get(cv.CV_CAP_PROP_FRAME_WIDTH)
height = capture.get(cv.CV_CAP_PROP_FRAME_HEIGHT)
scalex = 1366/width
scaley = 766/height
window  = laser_center(original_frame)
window = [scalex*window[0], scaley*window[1]]
root.warp_pointer(window[0], window[1])
d.sync()