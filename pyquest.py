from hand_tracking import tracking_hands, hands_json
import threading
import gestures

cam_thread = threading.Thread(target=tracking_hands)

cam_thread.start()

cam_thread.join()