# Hand Gesture Counter

A simple Computer Vision project that detects a hand from an image or webcam, counts raised fingers, and classifies the gesture from ZERO to FIVE.

## Features
- Hand landmark detection using MediaPipe
- Finger counting using landmark geometry
- Gesture classification (ZERO, ONE, TWO, THREE, FOUR, FIVE)
- Image mode for command-line evaluation
- Optional webcam mode
- Automated tests

## Requirements
- Python 3.10 or 3.11 recommended
- pip

## Installation

### Windows
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell blocks activation:
```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\.venv\Scripts\Activate.ps1
```

### Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run in image mode
```bash
python main.py --image sample/sample_hand.jpg
```

Image mode is recommended for evaluation because it does not require a webcam.

## Run with webcam
```bash
python main.py --webcam
```
Press `q` to quit.

## Run tests
```bash
pytest -q
```

## Project structure
```text
HandGestureCounter/
├── main.py
├── requirements.txt
├── README.md
├── statement.md
├── src/
│   ├── hand_detector.py
│   ├── finger_counter.py
│   ├── gesture_classifier.py
│   └── pipeline.py
├── tests/
├── docs/
└── sample/
```

## Output
Image mode creates `output/annotated_result.jpg` and `output/result.txt`.
The terminal prints the detected hand count, raised-finger count and gesture.

## Limitations
The classifier is designed for a clear single hand with reasonable lighting. Occlusion, unusual hand angles and multiple hands can reduce accuracy.
