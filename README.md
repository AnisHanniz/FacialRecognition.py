# Facial Recognition Application

This facial recognition application uses OpenCV to detect faces in real-time from a video feed. It applies image preprocessing techniques to improve detection accuracy.

## Features

- Real-time face detection from the camera feed.
- Draws rectangles around detected faces.
- Error handling to ensure smooth execution.

## Prerequisites

- Python 3.x
- OpenCV

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/AnisHanniz/facial-recognition-app.git
    cd facial-recognition-app
    ```

2. Install the dependencies:
    ```sh
    pip install opencv-python opencv-python-headless
    ```

## Usage

1. Run the script:
    ```sh
    python face_recognition.py
    ```

2. A video window will open, displaying the camera feed with rectangles drawn around detected faces.

3. To stop the application, press the `q` key or `ctrl+c`.
