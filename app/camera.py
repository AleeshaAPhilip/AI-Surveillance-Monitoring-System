import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
from app.status import status
from app.face_recognition import (
    known_face_encodings,
    known_face_names,
    log_event
)

camera = cv2.VideoCapture(0)

# ---------------- Configuration ----------------
MATCH_THRESHOLD = 0.55
FRAME_SKIP = 2          # Process every 2nd frame
LOG_COOLDOWN = 5        # Seconds
SAVE_COOLDOWN = 5       # Seconds
HOLD_TIME = 2           # Seconds to keep last recognized name

# ---------------- Runtime Variables ----------------
frame_counter = 0
face_locations = []
face_names = []

last_logged_person = None
last_unknown_save = None

last_recognized_name = "Unknown"
last_recognized_time = datetime.min


def generate_frames():
    global frame_counter
    global face_locations
    global face_names
    global last_unknown_save
    global last_recognized_name
    global last_recognized_time

    while True:

        success, frame = camera.read()

        if not success:
            break

        frame_counter += 1

        # ---------------- Face Recognition ----------------
        if frame_counter % FRAME_SKIP == 0:

            small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb)
            encodings = face_recognition.face_encodings(rgb, face_locations)

            face_names = []

            for encoding in encodings:

                name = "Unknown"

                if len(known_face_encodings) > 0:

                    distances = face_recognition.face_distance(
                        known_face_encodings,
                        encoding
                    )

                    best_index = np.argmin(distances)
                    best_distance = distances[best_index]

                    print(
                        f"Best Match : {known_face_names[best_index]}   "
                        f"Distance : {best_distance:.3f}"
                    )

                    if best_distance <= MATCH_THRESHOLD:
                        name = known_face_names[best_index]
                        last_recognized_name = name
                        last_recognized_time = datetime.now()
                        

                    else:
                        elapsed = (
                            datetime.now() - last_recognized_time
                        ).total_seconds()

                        if elapsed < HOLD_TIME:
                            name = last_recognized_name

                face_names.append(name)

        # ---------------- Draw Results ----------------
        for (top, right, bottom, left), name in zip(face_locations, face_names):

            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)

            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.rectangle(
                frame,
                (left, bottom - 35),
                (right, bottom),
                color,
                cv2.FILLED
            )

            cv2.putText(
                frame,
                name,
                (left + 6, bottom - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2
            )

            now = datetime.now()

            global last_logged_person

            if name != "Unknown":

                if last_logged_person != name:

                    log_event(name, "Known")

                    status["current_person"] = name
                    status["known_count"] += 1

                    last_logged_person = name

            else:

                if last_logged_person != "Unknown":

                    log_event("Unknown", "Intruder")

                    status["current_person"] = "Unknown"
                    status["unknown_count"] += 1

                    last_logged_person = "Unknown"

                if (
                    last_unknown_save is None
                    or
                    (now - last_unknown_save).total_seconds()
                    > SAVE_COOLDOWN
                ):

                    os.makedirs("unknown_faces", exist_ok=True)

                    filename = now.strftime("%Y%m%d_%H%M%S") + ".jpg"

                    cv2.imwrite(
                        os.path.join("unknown_faces", filename),
                        frame
                    )

                    last_unknown_save = now

        ret, buffer = cv2.imencode(".jpg", frame)

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'
            + buffer.tobytes()
            + b'\r\n'
        )
