import csv
import os
from datetime import datetime
from app.encoder import load_encodings

# Load cached encodings
known_face_encodings, known_face_names = load_encodings()


def log_event(person, status):

    os.makedirs("logs", exist_ok=True)

    logfile = "logs/events.csv"

    file_exists = os.path.isfile(logfile)

    with open(logfile, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Timestamp", "Person", "Status"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            person,
            status
        ])