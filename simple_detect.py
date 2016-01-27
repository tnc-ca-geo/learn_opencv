# see http://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/
import numpy as np
import cv2

cap = cv2.VideoCapture('test.mp4')
# see

# take first frame of the video
ret, frame = cap.read()

height, width, layers = frame.shape

# initialize average image
avg1 = np.float32(frame)
video = cv2.VideoWriter('video.avi', -1, 1, (width, height))

while(1):
    ret, frame = cap.read()
    img = None

    if ret == True:
        cv2.imshow('original', frame)
        # create moving average
        cv2.accumulateWeighted(frame, avg1, 0.02)
        res1 = cv2.convertScaleAbs(avg1)
        cv2.imshow('avg1', res1)

        img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        res1 = cv2.cvtColor(res1, cv2.COLOR_RGB2GRAY)
        frameDelta = cv2.absdiff(res1, img)
        blurred = cv2.GaussianBlur(frameDelta, (51, 51), 0)
        thresh = cv2.threshold(blurred, 30, 255, cv2.THRESH_BINARY)[1]
        cv2.imshow('copy', thresh)
        image, cnts, hierarchy = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in cnts:
            if cv2.contourArea(c) > 400:
                (x, y, w, h) = cv2.boundingRect(c)
                image = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.imshow('original', frame)
        video.write(image)

        k = cv2.waitKey(60) & 0xff
    else:
        break

cv2.destroyAllWindows()
cap.release()
video.release()
