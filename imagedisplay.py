#from VideoCapture import Device
import pygame
import cv2
import time
#In=1
pygame.init()
w = 2560
h = 1600
size=(w,h)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
#c = pygame.time.Clock() # create a clock object for timing

def showimage():
	filename = "test.jpg"
	img=pygame.image.load(filename) 
	screen.blit(img,(0,0))
	pygame.display.flip()

def closeimage():
	pygame.quit()

while True:
    #cam = Device()
    ##filename = "solidwhite.jpg" 
    #cam.saveSnapshot(filename) 
    ##img=pygame.image.load(filename) 
    ##screen.blit(img,(0,0))
    ##pygame.display.flip() # update the display
    #c.tick(3) # only three images per second
    #In += 1
    showimage()
    time.sleep(5)
    closeimage()
    break
#cv2.waitKey(10)    