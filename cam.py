import cv2
from gestures import up_index

cap = cv2.VideoCapture(1)

mirror = True

def return_frame():
    global mirror
    ret, frame = cap.read()

    if mirror:
        frame = cv2.flip(frame,1)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if up_index:
            cap.release()
            cv2.destroyAllWindows()

    elif cv2.waitKey(1) == ord('m'):
        mirror = not mirror


    return frame, frame_rgb