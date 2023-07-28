import numpy as np
import pyautogui
import cv2


resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"H264")
filename = "Recording.mp4"
fps = 60.0
out = cv2.VideoWriter(filename, codec, fps, resolution)
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

try:
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow('Live', frame)
        if cv2.waitKey(1) == ord('q'):
            break

finally:
