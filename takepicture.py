import cv2
import time
cam = cv2.VideoCapture(0)
cam.set(3,1280)
cam.set(4,1024)

def photographer():
	cv2.namedWindow("Calibrating")
	ret, frame = cam.read()
	#cv2.imshow("test", frame)
	time.sleep(2)
	img_name = "calibration.jpg"
	cv2.imwrite(img_name, frame)
	print("{} written!".format(img_name))
	cam.release()
	cv2.destroyAllWindows()

while True:
	photographer()
	#ret, frame = cam.read()
	#cv2.imshow("test", frame)
	#time.sleep(2)
	#img_name = "test.jpg"
	#cv2.imwrite(img_name, frame)
	#print("test written!")
	cam.release()
	cv2.destroyAllWindows()
	break