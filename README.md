# OpenCV Projects

This folder contains various Python scripts using the OpenCV library for different computer vision tasks. Below is a brief description of each script:

## 1. `colour_detection.py`
This script detects and identifies specific colors within an image or video feed. It can be used to filter out or highlight colors based on predefined ranges in the HSV color space.

**Usage:**
- Load an image or video.
- The script processes the image to detect the specified colors.
- The detected colors are highlighted or isolated in the output.

## 2. `face_detection.py`
This script detects faces in images or video streams using OpenCV's pre-trained Haar Cascade classifiers.

**Usage:**
- Load an image or a video feed.
- The script scans for faces and draws bounding boxes around any detected faces.
- The result is displayed with the detected faces highlighted.


## 3. `lines_and_texts.py`
This script is designed to detect lines and text within an image using techniques like Hough Line Transform and image processing filters.

**Usage:**
- Load an image containing lines or text.
- The script detects and draws the lines on the image.
- Text detection can also be applied depending on the implementation.

---

## Installation and Requirements

Before running the scripts, make sure you have the required dependencies installed. You can install them using the following command:
Ensure that the OpenCV library is installed:

```bash
pip install opencv-python
```

## Running the Scripts

Each script can be run individually from the command line:

```bash
python <script_name>.py
```

Replace `<script_name>` with the name of the script you wish to run, e.g., `python face_detection.py`.

---

