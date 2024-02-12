

import cv2
import os

# Create a directory to store the captured images
directory = input("Enter the name of the individual: ")
os.makedirs(directory, exist_ok=True)

# Initialize the OpenCV video capture
cap = cv2.VideoCapture(0)

# Load the pre-trained face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the counter to keep track of captured images
counter = 0

while counter < 200:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the captured frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Crop and save the detected faces
    for (x, y, w, h) in faces:
        face_crop = frame[y:y+h, x:x+w]
        image_path = os.path.join(directory, f"image{counter}.jpg")
        cv2.imwrite(image_path, face_crop)
        counter += 1
        print(f"Image {counter} captured and saved")

    # Display the captured frame
    cv2.imshow('Capture', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
