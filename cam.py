import cv2

cap = cv2.VideoCapture(1)

mirror = True

def return_frame():
    global mirror
    ret, frame = cap.read()

    if mirror:
        frame = cv2.flip(frame,1)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if cv2.waitKey(1) == 27:
            cap.release()
            cv2.destroyAllWindows()

    elif cv2.waitKey(1) == ord('m'):
        mirror = not mirror


    return frame, frame_rgb