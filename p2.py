import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

# To use the webcam on your computer
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img = cap.read()
