import os, sys
import random
import pygame
import time
import cv2 as cv
from pygame.locals import *

def onetrickpony(x1,y1,x2,y2):
	#x = x1
	#y = y1
	os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x1,y1)
	print(x1,y1)
	pygame.init()
	APPLICATION_x_size = x2-x1
	APPLICATION_y_size = y2-y1
	screen = pygame.display.set_mode((APPLICATION_x_size, APPLICATION_y_size), pygame.NOFRAME)
	black_square_that_is_the_size_of_the_screen = pygame.Surface(screen.get_size())
	black_square_that_is_the_size_of_the_screen.fill((0, 0, 0))
	#screen.blit(black_square_that_is_the_size_of_the_screen, (0, 0))


def draw_rects(rects):
    for x1, y1, x2, y2 in rects:
        #cv.rectangle(img, (x1, y1), (x2, y2), color, -1)
        onetrickpony(x1,y1,x2,y2)


if __name__ == "__main__":
	testrects = [[670, 309, 831, 470]]
	draw_rects(testrects)
	time.sleep(5)
