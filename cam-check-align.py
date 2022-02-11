#camera alignment/focusing tool - streams video from camera, stops when Q key is pressed
from cv2 import *

cam_port = input("Set input camera: ")
cap = VideoCapture(cam_port)

if not (cap.isOpened()):
	print("Could not open video device")

while(True):
	ret, frame = cap.read()

	imshow('preview', frame)

	if waitKey(1) & 0xFF == ord('q'):
		break

cap.release()