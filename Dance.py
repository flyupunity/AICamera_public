import mediapipe as mp
import cv2

# Create a face detector instance
face_detector = mp.solutions.face_detection.FaceDetection()

# Open the camera stream
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        break

    # Convert the image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect faces in the image
    results = face_detector.process(image_rgb)

    # Check if multiple faces are detected
    if results.detections and len(results.detections) > 1:
        print("Multiple faces detected.")

    # Display the image with face detections
    cv2.imshow("Face Detection", image)
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
