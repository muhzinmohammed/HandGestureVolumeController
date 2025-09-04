# Hand Gesture Volume Controller

A Python application that allows you to **control system volume using hand gestures** in real-time. The script uses **MediaPipe** for hand tracking, **OpenCV** for video capture, and **PyCaw** for audio control. .

---

## Features

- Tracks **thumb and index finger** to control volume.  
- **Global hotkey** support to stop the program from any window (`Ctrl + Q + W`).  

---

## Installation

Install the required Python packages:

```bash
pip install opencv-python mediapipe pycaw comtypes keyboard numpy
