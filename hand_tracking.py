import cv2

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

import cam

# load model
base_options = python.BaseOptions(
    model_asset_path="./models/hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=2
)

detector = vision.HandLandmarker.create_from_options(options)

HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (5,9),(9,10),(10,11),(11,12),
    (9,13),(13,14),(14,15),(15,16),
    (13,17),(17,18),(18,19),(19,20),
    (0,17)
]

hands_position = {
        "left": None,
        "right":None
}
points = []

def tracking_hands():
    while True:

        hands_position = {
        "left": None,
        "right":None
}


        frame , frame_rgb = cam.return_frame()

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=frame_rgb
        )

        result = detector.detect(mp_image)

        if result.hand_landmarks:

            h, w, _ = frame.shape

            for index,hand in enumerate(result.hand_landmarks):

                points = []

                label = result.handedness[index][0].category_name

                # draw points
                for lm in hand:
                    x = int(lm.x * w)
                    y = int(lm.y * h)

                    points.append((x,y))

                    cv2.circle(frame,(x,y),5,(90,0,180),-1)

                    # print(label)
 
                # draw connections
                for connection in HAND_CONNECTIONS:
                    start = points[connection[0]]
                    end = points[connection[1]]

                    cv2.line(frame,start,end,(100,100,200),2)

                if label == "Right":
                    hands_position["right"] = fill_data(points)
                if label == "Left":
                    hands_position["left"] = fill_data(points)
        cv2.imshow("Hand Tracking", frame)
        # print(hands_position)


def hands_json():
    if hands_position["left"] != None:
        return hands_position, "left"
    elif hands_position["right"] != None:
        return hands_position, "right"
    elif hands_position["right"] != None and hands_position["left"] != None:
        return hands_position, "left-right"
    return None, ""
    
# hand -> left -> fingers -> thump -> tip = x,y
def fill_data(points):
    return {"wrist": points[0],
            "fingers": {
                "thumb":points[1:5],
                "index":points[5:9],
                "middle":points[9:13],
                "ring":points[13:17],
                "pinky":points[17:21]
                    }
                }