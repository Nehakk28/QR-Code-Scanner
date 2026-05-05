# QR Code Scanner (OpenCV)

A simple and efficient **QR Code Scanner** built using **Python and OpenCV**.
This project uses your webcam to scan QR codes in real-time and saves the scanned data to a file.

## Features
- Real-time QR code detection using webcam
- Displays scanned data on screen
- Saves scanned results to a text file
- Lightweight and easy to run
- No external DLL dependencies

## Tech Stack

- Python
- OpenCV

---

## Project Structure

QR-Code-Scanner/
│
├── Model/
│   ├── qrcodereader_opencv.py
│   └── scanned_result.txt
│
├── LICENSE
├── README.md
└── .gitignore

<pre> QR-Barcode-Scanner/ ├── Model/ │ ├── qrcodereader_opencv.py │ └── scanned_result.txt ├── LICENSE ├── README.md └── .gitignore </pre>

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/QR-Code-Scanner.git
```

2. Navigate to the project folder:

```
cd QR-Code-Scanner/Model
```

3. Install dependencies:

```
pip install opencv-python
```

### How to Run

```
python qrcodereader_opencv.py
```
- Press **ESC** to exit
- Scanned results will be saved in `scanned_result.txt`

## License

This project is licensed under the **Apache License 2.0**.

