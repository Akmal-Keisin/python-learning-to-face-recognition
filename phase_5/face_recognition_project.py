import face_recognition
import cv2

cap = cv2.VideoCapture(0)
frame_count = 0
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

person_photo = face_recognition.load_image_file("known_faces/akmalkeisin.jpg")
person_photo_encoding = face_recognition.face_encodings(person_photo)[0]
known_encoding = [
	person_photo_encoding
]

while True:
	ret, frame = cap.read()
	if not ret:
		break

	grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	small = cv2.resize(grey, (0, 0), fx=0.5, fy=0.5)
	rgb_small = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

	if frame_count % 5 == 0:  # Process every 5th frame
		faces = face_cascade.detectMultiScale(rgb_small, scaleFactor=1.1, minNeighbors=5)

	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x * 2, y * 2), ((x + w) * 2, (y + h) * 2), (0, 255, 0), 2)
		cv2.putText(frame, "Face Detected", (x * 2, y * 2 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

	frame_count += 1
	cv2.imshow('Webcam', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	if cv2.waitKey(1) & 0xFF == ord('c'):
		print("Capturing face for recognition...")
			
		# Find all the faces and face encodings in the current frame of video
		face_locations = face_recognition.face_locations(rgb_small)
		face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

		matches = []
		for face_encoding in face_encodings:
			matches = face_recognition.compare_faces(known_encoding, face_encoding)

		if True in matches:
			print("Face recognized!")
			break
		
cap.release()
cv2.destroyAllWindows()
