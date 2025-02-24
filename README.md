# 🚀 YOLO PotHole Detection (Real-Time Streaming)

## 📌 Project Overview
This project utilizes the **YOLO model** to detect objects in uploaded videos and visualize them in real-time.  
**The Gradio-based web UI allows users to upload videos and view detection results instantly.**  
**Only `UI.ipynb` and `best.pt` are required to run the project!**  

---

## 🛠️ Installation

### Required Packages
To run the project, install the following dependencies:  

```pip install ultralytics gradio opencv-python numpy```

💡 Ultralytics is required for YOLO model execution.

💡 Gradio is used for creating the web-based UI.

### Required Files

UI.ipynb → Jupyter Notebook containing the Gradio interface code
best.pt → Pretrained YOLO model weights
With these two files, you can run the project without any additional setup.

### 🔄 Workflow
1️⃣ Upload a Video

Users can upload a video via the web UI.
A default example video (output_videos/processed_cityRoad_potHoles.mp4) is preloaded.

2️⃣ Start AI Detection

Press the "🚀 Start AI Detection!" button to begin YOLO-based object detection.
The model processes video frames, detects objects, and draws bounding boxes in real-time.

3️⃣ Adjust Frame Skipping

The frame_skip slider allows users to control detection speed.
Lower values (e.g., 1) detect objects in every frame (higher accuracy but slower).
Higher values (e.g., 10) skip more frames, increasing speed at the cost of accuracy.

4️⃣ View Processed Video Stream

The processed video stream is displayed directly in the Gradio interface.
Users can visually analyze detected objects without needing to download the output.

