from hand_tracking import tracking_hands
import threading
from cam import return_frame
import cv2

cam_thread = threading.Thread(target=tracking_hands)

cam_thread.start()

cam_thread.join()