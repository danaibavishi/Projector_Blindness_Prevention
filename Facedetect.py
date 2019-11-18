#!/usr/bin/env python

'''
face detection using haar cascades

USAGE:
    facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv

# local modules
#from video import create_capture
from common import clock, draw_str
import Picasso

def create_capture(source = 0):
    '''source: <int> or '<int>|<filename>|synth [:<param_name>=<value> [:...]]'
    '''
    source = str(source).strip()
    chunks = source.split(':')
    # handle drive letter ('c:', ...)
    if len(chunks) > 1 and len(chunks[0]) == 1 and chunks[0].isalpha():
        chunks[1] = chunks[0] + ':' + chunks[1]
        del chunks[0]

    source = chunks[0]
    try: source = int(source)
    except ValueError: pass
    params = dict( s.split('=') for s in chunks[1:] )

    cap = None
    if source == 'synth':
        Class = classes.get(params.get('class', None), VideoSynthBase)
        try: cap = Class(**params)
        except: pass
    else:
        cap = cv.VideoCapture(source)
            #w, h = map(int, params['size'].split('x'))
        cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
    if cap is None or not cap.isOpened():
        print('Warning: unable to open video source: ', source)
    return cap

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects


def detectionloop():
	pass

if __name__ == '__main__':
	#detectionloop()
    import sys, getopt
    print(__doc__)

    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try:
        video_src = video_src[0]
    except:
        video_src = 0
    args = dict(args)
    cascade_fn = args.get('--cascade', "/Users/Danai/Desktop/opencvnew/data/haarcascades/haarcascade_frontalface_alt.xml")
    nested_fn  = args.get('--nested-cascade', "/Users/Danai/Desktop/opencvnew/data/haarcascades/haarcascade_eye.xml")

    cascade = cv.CascadeClassifier(cascade_fn)
    nested = cv.CascadeClassifier(nested_fn)

    cam = create_capture(video_src)
    while True:
        ret, img = cam.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray = cv.equalizeHist(gray)

        t = clock()
        rects = detect(gray, cascade)
        vis = img.copy()
        #draw_rects(vis, rects, (0, 0, 0))
        #This is where the picasso comes in 
        Picasso.draw_rects(rects)
        #dt = clock() - t

        #draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
        cv.imshow('facedetect', vis)

        if cv.waitKey(5) == 27:
            break
    cv.destroyAllWindows()










