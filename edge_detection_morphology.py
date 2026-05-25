import cv2
import numpy as np
# Start video capture
cap = cv2.VideoCapture(0)  # Use webcam (change the argument for other cameras or video files)

# Define the kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

while True:
    # Capture each frame from the video feed
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray_frame, 100, 200)

 # Perform dilation on the edges
    dilated_edges = cv2.dilate(edges, kernel, iterations=1)


 # Perform erosion on the edges (students to complete this)
    eroded_edges = cv2.erode(edges, kernel, iterations=1)


    # Display the original frame and processed results
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Edges', edges)
   
# Add two more cv2.imshow() calls to display the dilated and eroded edges
    cv2.imshow('Dilated Edges', dilated_edges)
    cv2.imshow('Eroded Edges', eroded_edges) 

    # Exit the application when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()