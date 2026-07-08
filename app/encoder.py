import os
import pickle
import face_recognition

ENCODING_FILE = "encodings/encodings.pkl"


def generate_encodings():

    known_face_encodings = []
    known_face_names = []

    base_folder = "known_faces"

    for person in os.listdir(base_folder):

        person_folder = os.path.join(base_folder, person)

        if not os.path.isdir(person_folder):
            continue

        for image_name in os.listdir(person_folder):

            if not image_name.lower().endswith((".jpg", ".jpeg", ".png")):
                continue

            image_path = os.path.join(person_folder, image_name)

            image = face_recognition.load_image_file(image_path)

            encodings = face_recognition.face_encodings(image)

            if len(encodings) == 0:
                continue

            known_face_encodings.append(encodings[0])
            known_face_names.append(person)

    os.makedirs("encodings", exist_ok=True)

    with open(ENCODING_FILE, "wb") as f:

        pickle.dump(
            {
                "encodings": known_face_encodings,
                "names": known_face_names
            },
            f
        )

    print("Encodings saved successfully!")


def load_encodings():

    with open(ENCODING_FILE, "rb") as f:

        data = pickle.load(f)

    return data["encodings"], data["names"]