import cv2
import pyvirtualcam

# Initialize the camera capture
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Get the width, height, and fps from the camera capture
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Create a virtual camera with the same width, height, and fps
with pyvirtualcam.Camera(width=width, height=height, fps=fps) as cam:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if frame is captured successfully
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert the frame to RGB (pyvirtualcam expects RGB)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Send the RGB frame to the virtual camera
        cam.send(frame_rgb)
        cam.sleep_until_next_frame()

        # Display the frame
        cv2.imshow('Video', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the camera capture and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
