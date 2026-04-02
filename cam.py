import cv2

cap = cv2.VideoCapture(1)

def return_frame():

    ret, frame = cap.read()

    # frame = cv2.flip(frame,1)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if cv2.waitKey(1) == 27:
            cap.release()
            cv2.destroyAllWindows()

    return frame, frame_rgb