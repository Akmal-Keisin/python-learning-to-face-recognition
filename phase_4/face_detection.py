import cv2

# Load the face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Open webcam
cap = cv2.VideoCapture(0)
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    small = cv2.resize(gray, (0, 0), fx=0.5, fy=0.5)

    # Detect faces
    if frame_count % 5 == 0:  # Process every 5th frame
        faces = face_cascade.detectMultiScale(small, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x * 2, y * 2), ((x + w) * 2, (y + h) * 2), (0, 255, 0), 2)

    # Show frame
    cv2.imshow("Face Detection", frame)
    
    key = cv2.WaitKey(1) & 0xFF

    # Exit on 'q'
    if key == ord('q'):
        break
    
    if key == ord('c'):
        cv2.imwrite("images/captured_face.jpg", frame)
        break

cap.release()
cv2.destroyAllWindows()
