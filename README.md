# 🛡️ AI Surveillance & Monitoring System

An AI-powered surveillance system that performs **real-time face recognition**, **intruder detection**, and **live video monitoring** using **Raspberry Pi**, **OpenCV**, and **Flask**.

The Raspberry Pi captures live video from a USB webcam and streams it over the local network, while a laptop performs face recognition using cached face encodings, detects unknown visitors, logs events, and displays the results through a web dashboard.

---

## 📌 Features

- 🎥 Live video streaming from Raspberry Pi
- 😀 Real-time face recognition
- 👥 Multiple known persons support
- 🚨 Unknown intruder detection
- 📸 Automatic unknown face image capture
- 📝 Event logging with timestamps
- 🌐 Live Flask web dashboard
- ⚡ Cached face encodings for faster startup
- 🚀 Frame skipping for improved performance
- 💻 Simple and clean user interface

---

# 🏗️ System Architecture

```
             USB Webcam
                  │
                  ▼
          Raspberry Pi 4
                  │
      OpenCV Video Capture
                  │
      Flask Video Streaming
                  │
        Local Wi-Fi Network
                  │
                  ▼
             Laptop (Python)
                  │
      Face Recognition Engine
                  │
     ┌────────────┴────────────┐
     │                         │
Known Person             Unknown Person
     │                         │
     │                   Save Image
     │                   Log Event
     │                         │
     └────────────┬────────────┘
                  │
                  ▼
          Flask Web Dashboard
```

---

# 📂 Project Structure

```
AI-Surveillance-Monitoring-System
│
├── app/
│   ├── app.py
│   ├── camera.py
│   ├── encoder.py
│   ├── face_recognition.py
│   ├── status.py
│   └── config.py
│
├── known_faces/
├── unknown_faces/
├── encodings/
├── logs/
├── static/
├── templates/
│
├── generate_encodings.py
├── run.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🛠️ Technologies Used

- Python
- Raspberry Pi 4
- OpenCV
- Flask
- face_recognition
- NumPy
- HTML
- CSS
- JavaScript

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/AleeshaAPhilip/AI-Surveillance-Monitoring-System.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 👥 Add Known Faces

Place images inside

```
known_faces/
```

Example

```
known_faces/
    Anne/
        1.jpg
        2.jpg
        3.jpg
```

---

# ⚡ Generate Face Encodings

```bash
python generate_encodings.py
```

This creates

```
encodings/encodings.pkl
```

---

# ▶️ Run the Project

```bash
python run.py
```

Open

```
http://127.0.0.1:5000
```

---

# 📋 Event Logging

Every detection is stored in

```
logs/events.csv
```

Example

| Timestamp | Person | Status |
|-----------|--------|--------|
| 2026-07-09 10:20 | Anne | Known |
| 2026-07-09 10:24 | Unknown | Intruder |

---

# 🚨 Unknown Face Storage

Whenever an unknown person is detected, an image is automatically saved inside

```
unknown_faces/
```

---

# 🔮 Future Improvements

- Email alerts
- Mobile notifications
- Cloud database integration
- GPU acceleration
- Multiple camera support

---

# 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Aleesha A Philip**

Robotics & Automation Engineering Undergraduate

Lovely Professional University