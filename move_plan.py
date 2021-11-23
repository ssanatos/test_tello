from djitellopy import Tello

# https://djitellopy.readthedocs.io/en/latest/tello/

tello = Tello()

tello.connect()

tello.takeoff()

# 단위가 cm
tello.move_up(150)

tello.move_forward(200)

# 단위가 deg
tello.rotate_clockwise(360)

tello.move_back(100)

tello.land()

pass