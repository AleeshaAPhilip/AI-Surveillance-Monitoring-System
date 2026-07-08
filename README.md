# AI Surveillance & Monitoring System

An AI-powered surveillance system that performs real-time face recognition and intruder detection using Raspberry Pi, OpenCV, Flask, and Python. The Raspberry Pi captures live video from a USB webcam and streams it over the local network, while a laptop performs face recognition, logs events, and provides a web-based monitoring dashboard.

---

## Features

- Real-time video streaming from Raspberry Pi
- Face recognition using cached face encodings
- Automatic intruder detection
- Unknown face image storage
- Event logging with timestamps
- Live web dashboard using Flask
- Multiple known persons supported
- Cached face encodings for faster startup
- Frame skipping for improved performance

---

## Technologies Used

- Python
- OpenCV
- Flask
- face_recognition
- NumPy
- HTML
- CSS
- JavaScript
- Raspberry Pi 4

---

## Project Structure

```text
AI-Surveillance-Monitoring-System
│
├── app/
├── known_faces/
├── encodings/
├── unknown_faces/
├── logs/
├── static/
├── templates/
├── screenshots/
├── run.py
├── generate_encodings.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Surveillance-Monitoring-System.git
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Generate Face Encodings

Add images inside:

```text
known_faces/
```

Then run

```bash
python generate_encodings.py
```

This creates

```text
encodings/encodings.pkl
```

---

## Run the Project

```bash
python run.py
```

Open

```
http://127.0.0.1:5000
```

---

## Future Improvements

- Email alerts for intruder detection
- Cloud event storage
- Mobile notification support
- GPU acceleration
- Face mask detection

---

## License

This project is released under the MIT License.