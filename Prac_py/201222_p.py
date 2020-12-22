from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())


# 해당 경로에 있는 동영상 파일에서 프레임을 받아온다. 
capture = cv2.VideoCapture("../ex_file/sample.mp4")

# 현재 프레임 수와 총 프레임 수를 비교한다. 
# capture.get(속성)을 이용하여 capture의 속성을 가져온다. 
# CAP_PROP_POS_FRAMES = 현재 프레임 개수
# CAP_PROP_POS_FRAME_COUNT = 총 프레임 개수
# 같을 경우 마지막 프레임이므로 capture.open(경로)를 이용하여 다시 동영상 파일을 불러온다.


while True:
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)): 
        capture.open("../ex_file/sample.mp4")

    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    if cv2.waitKey(33) > 0: break

capture.release()
cv2.destroyAllWindows()