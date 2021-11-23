from djitellopy import Tello
import cv2

# tello = Tello()

# tello.connect()

# tello.streamon()

# # move control with keyboard
# while True:
#     frame_read = tello.get_frame_read()
#     cv2.imshow('tello stream',frame_read.frame)
#     key = cv2.waitKey(1)
#     if key > -1:
#         print('input = ',key)
#         if key == ord('q'):
#             tello.land()
#             tello.streamoff()
#             break
#         elif key == ord('t'):
#             tello.takeoff()
#         # 스페이스바로 착륙
#         elif key == 32:
#             tello.land()
#         # wasd로 상하회전
#         elif key == ord('w'):
#             tello.move_up(20)
#         elif key == ord('a'):
#             tello.rotate_counter_clockwise(30)
#         elif key == ord('d'):
#             tello.rotate_clockwise(30)
#         elif key == ord('s'):
#             tello.move_down(20)
#         # 방향키로 전후좌우 조정
#         elif key == 81:
#             tello.move_left(30)
#         elif key == 82:
#             tello.move_forward(30)
#         elif key == 83:
#             tello.move_right(30)
#         elif key == 84:
#             tello.move_back(30)
# pass




def drone():
    tello = Tello()

    tello.connect()

    tello.streamon()

    # move control with keyboard
    while True:
        frame_read = tello.get_frame_read()
        cv2.imshow('tello stream',frame_read.frame)
        key = cv2.waitKey(1)
        if key > -1:
            print('input = ',key)
            if key == ord('q'):
                tello.land()
                tello.streamoff()
                break
            elif key == ord('t'):
                tello.takeoff()
            # 스페이스바로 착륙
            elif key == 32:
                tello.land()
            # wasd로 상하회전
            elif key == ord('w'):
                tello.move_up(20)
            elif key == ord('a'):
                tello.rotate_counter_clockwise(30)
            elif key == ord('d'):
                tello.rotate_clockwise(30)
            elif key == ord('s'):
                tello.move_down(20)
            # 방향키로 전후좌우 조정
            elif key == 81:
                tello.move_left(30)
            elif key == 82:
                tello.move_forward(30)
            elif key == 83:
                tello.move_right(30)
            elif key == 84:
                tello.move_back(30)
    pass

drone()