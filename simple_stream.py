from djitellopy import Tello
import cv2

tello = Tello()

tello.connect()

tello.streamon()

# tello video
while True:
    # tello.takeoff()
    frame_read = tello.get_frame_read()
    cv2.imshow('tello stream',frame_read.frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
tello.streamoff()
# tello.land()
pass