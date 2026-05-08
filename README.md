# YouTube Tutorial Codes

This repository contains source code and example projects from the Tech Watt YouTube tutorials. It brings together computer vision, deep learning, automation, and Python mini-projects so viewers can follow along with the videos and experiment with the code locally.

## What You Will Find

The repository is organized by tutorial topic. Each folder or script contains the files used in a specific video or playlist.

### Tutorial Folders

| Folder | Topic |
| --- | --- |
| `Ai dumbell trainer` | AI fitness / dumbbell curl trainer project |
| `Fire Detector Course` | Fire detection with computer vision |
| `LINE DETECTION` | Line detection examples |
| `Push ups` | Push-up counter / pose estimation project |
| `YOLONAS COURSE` | YOLO-NAS object detection tutorials |
| `Yolo in IDE` | Running YOLO projects in an IDE |
| `bottle detection` | Bottle detection project |
| `dino game` | Computer vision / automation game project |
| `finger up counter` | Hand tracking and finger counting |
| `game` | Python game-related tutorial code |
| `pytorch SSD Model` | SSD object detection with PyTorch |
| `text extraction` | Text extraction / OCR examples |
| `vehicle detection and counting coures` | Vehicle detection and counting tutorials |
| `yolov4` | YOLOv4 examples |
| `yolov8 in colab` | YOLOv8 examples for Google Colab |

### Standalone Scripts

| File | Description |
| --- | --- |
| `Eye detection.py` | Detects and marks eye landmarks using OpenCV and cvzone pose detection. |
| `Gesture screen britness control.py` | Gesture-based screen brightness control project. |
| `QR-CODE-SCANNER.py` | Real-time QR code and barcode scanner using OpenCV, cvzone, and pyzbar. |
| `Youtube_transcript_downloader.py` | Downloads and prints transcript text from a YouTube video. |

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Tech-Watt/YOUTUBE-TUTORIAL-CODES.git
cd YOUTUBE-TUTORIAL-CODES
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

Different tutorials use different libraries. Install the packages required by the project you want to run.

Common packages used across the tutorials include:

```bash
pip install opencv-python cvzone numpy mediapipe pyzbar youtube-transcript-api
```

Some deep learning projects may also require packages such as:

```bash
pip install torch torchvision ultralytics
```

For YOLO-NAS or other specialized models, check the files inside that tutorial folder and install the matching library versions used in the video.

## How to Run a Tutorial

Open the folder for the tutorial you are following, then run the main Python file for that project.

Example:

```bash
python "QR-CODE-SCANNER.py"
```

For folders with spaces in the name, wrap the path in quotes:

```bash
cd "vehicle detection and counting coures"
```

Many computer vision projects use a webcam. Make sure your camera is connected and available before running those scripts.

## Notes

- This repository is a learning resource for YouTube tutorials, so projects may be kept close to the video code for easier follow-along.
- Some scripts may require model weights, videos, images, or datasets that are explained in the related tutorial.
- If a project uses Google Colab, open the notebook or script from the matching folder and follow the video setup steps.
- For best results, use a separate virtual environment for each larger project.

## Recommended Workflow

1. Open the tutorial video.
2. Find the matching folder or script in this repository.
3. Install the required dependencies.
4. Run the code and test it with your own images, videos, or webcam.
5. Modify the code to build your own version of the project.

## Topics Covered

- Python programming
- OpenCV
- Computer vision
- Object detection
- Pose estimation
- Hand tracking
- OCR and text extraction
- YOLOv4, YOLOv8, and YOLO-NAS
- PyTorch object detection
- AI-powered automation projects

## Author

Created by [Tech Watt](https://github.com/Tech-Watt) for YouTube tutorial projects.

## License

No license file is currently included. If you plan to reuse this code in your own project, please check the repository status or contact the author first.
