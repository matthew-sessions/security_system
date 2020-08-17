from pyimagesearch.motion_detection import SingleMotionDetector
from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import datetime
import imutils
import time
import cv2

outputFrame = None
lock = threading.Lock()


vs = VideoStream(src=0).start()
time.sleep(2.0)

def detect_motion(frameCount):
    # grab global references to the video stream, output frame, and
    # lock variables
    global vs, outputFrame, lock

    # initialize the motion detector and the total number of frames
    # read thus far
    md = SingleMotionDetector(accumWeight=0.5)
    total = 0

    frame_array = []
    frame_counter = 0
    has_motion = False
    last_motion = datetime.datetime.now()



    # loop over frames from the video stream
    while True:
        # read the next frame from the video stream, resize it,
        # convert the frame to grayscale, and blur it
        full_frame = vs.read()
    
        frame_array.append(full_frame)
        frame_counter += 1
        if frame_counter % 1000 == 0:

                    
            #save_video(frame_counter, frame_array)
            frame_array = frame_array[-1000:]

        
        frame = imutils.resize(full_frame, width=400)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #gray = gray[110:230, 106:250]
        gray = cv2.GaussianBlur(gray, (7, 7), 0)

        # grab the current timestamp and draw it on the frame
        timestamp = datetime.datetime.now()
        cv2.putText(frame, timestamp.strftime(
            "%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

        # if the total number of frames has reached a sufficient
        # number to construct a reasonable background model, then
        # continue to process the frame

        if total > frameCount:
            # detect motion in the image
            motion = md.detect(gray)

            # cehck to see if motion was found in the frame
            if motion is not None:
                if datetime.datetime.now() > last_motion + datetime.timedelta(seconds=2):
                    print(total)
                last_motion = datetime.datetime.now()
                # unpack the tuple and draw the box surrounding the
                # "motion area" on the output frame
                # (thresh, (minX, minY, maxX, maxY)) = motion
                # cv2.rectangle(frame, (minX, minY), (maxX, maxY),
                # 	(0, 0, 255), 2)
        
        # update the background model and increment the total number
        # of frames read thus far
        md.update(gray)
        total += 1
        

        # acquire the lock, set the output frame, and release the
        # lock
        # cv2.imshow('k', frame)
        cv2.imshow('d', full_frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
detect_motion(32)