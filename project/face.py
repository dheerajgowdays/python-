import cv2

# Load the Haar Cascade face detector
a = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Start video capture (0 = default webcam)
b = cv2.VideoCapture(0)

while True:
    c_rec, d_image = b.read()  # Read frame from webcam
    e = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    f = a.detectMultiScale(e, scaleFactor=1.3, minNeighbors=6)

    # Draw rectangle around detected faces
    for (x1, y1, w1, h1) in f:
        cv2.rectangle(d_image,(x1, y1),(x1 + w1, y1 + h1),(256, 0, 0), 5)

    # Show video frame
    cv2.imshow('img', d_image)

    # Press 'q' to quit
    d = cv2.waitKey(40) & 0xff
    if d == ord('q'):
        break

b.release()
cv2.destroyAllWindows()
