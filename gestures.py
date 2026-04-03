from hand_tracking import hands_json

hand , side = hands_json()

def up_index():
    if "right" in side:
        if hand["right"]["fingers"]["index"][3][1] > hand["right"]["fingers"]["index"][2][1]:
            return True
        