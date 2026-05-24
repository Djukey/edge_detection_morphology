# edge_detection_morphology

This project is a real-time edge detection and morphological operations

**Artificial Intelligence in computer vision**


This project is a real-time edge-detection app I built for week 2 of my computer vision assignment. 
When you run the script, it opens your webcam and pops up 4 windows: 
- First is the **original frame**
- Second is **the edges** (white lines on black, showing where the boundaries are)
- Third is **Dialeted Edges**  (the same edges but thicker and more connected)
- The last window is for **eroded edges**

As soon as you have completed the process, you can press **Q** to quit.

**How does it work?**

The code continuously grabs each frame from the webcam. The code converts it into grayscale because we don't need colors, just brightness. Runs cv2.Canny() with thresholds 100 and 200 to find the edges. Runs cv2.dilate() to thicken those edges using a 5x5 kernel. Runs cv2.erode() to thin those edges using the kernel. At the end, the code shows all 4 windows side by side. Press Q to exit

**Files**

edge_detection_morphology.py is the main script

**How to run the code?**

You'll need to install Python and OpenCV, then run: python edge_detection_morphology.py 

**My setup**

Windows laptop

Anaconda environment called cv-week1

OpenCV installed with pip install opencv-python


Heads up: I originally tried to run OpenCV with conda install -c conda-forge opencv, but the cv2.imshow() windows wouldn't display. If you are using a conda environment, you will likely need GTK or Cocoa support. The simple idea is to switch to pip install opencv-python. 

Send me your feedbacks

**Thanks>**



