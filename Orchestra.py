import imagedisplay
import takepicture
import detect_shapes

if __name__ == "__main__":
	imagedisplay()
	time.sleep(1)
	takepicture()
	time.sleep(1)
	detect_shapes.detectshapes("calibration.jpg")
	cv2.waitKey(0)
	break





#call facedetect, in fa
#create a graceful way to end the script 