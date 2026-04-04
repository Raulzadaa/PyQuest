from hand_tracking import hands_to_json

hand_json , side = hands_to_json()

def up_index():
    # print("entrou na funcao", side)
    if (side != ""):
        if hand_json[side]["fingers"]["index"]["tip"][1] > hand_json["right"]["fingers"]["index"]["dip"][1]:
            return True