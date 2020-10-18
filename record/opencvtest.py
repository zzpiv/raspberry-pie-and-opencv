import cv2
import numpy as np

COLOR_MAP = {
    "blue": (255, 0, 0),
    "green": (0, 255, 0),
    "red": (0, 0, 255),
    "white": (255, 255, 255)
}

def InitPaint(width, height, color=COLOR_MAP["white"]):
    paint = np.ones((height, width, 3), dtype="uint8")
    paint[:] = color
    return paint

paint = InitPaint(300, 300)

cv2.line(paint, pt1=(0, 0), pt2=(300, 300), color=COLOR_MAP["green"])

cv2.circle(paint, center=(150, 150), radius=50, color=COLOR_MAP["green"])

cv2.circle(paint, (150, 150), 30, color=COLOR_MAP["blue"], thickness=-1)

cv2.rectangle(paint, (10, 10), (60, 60), COLOR_MAP['red'])

points = np.array([[100,50],[200,200],[270,200],[290,100]], np.int32)

points = points.reshape((-1,1,2))

cv2.polylines(paint, pts=[points], isClosed=True, color=COLOR_MAP["red"], thickness=3)

cv2.ellipse(img=paint,center=(256,256), axes=(40,20), angle=0, startAngle=0, endAngle=360, color=(100, 200, 0), thickness=-1)

font = cv2.FONT_HERSHEY_SIMPLEX

line = cv2.LINE_AA

cv2.putText(img=paint, text="Hello", org=(10, 250), fontFace=font, fontScale=2, color=(0, 0, 255),thickness=1, lineType=line)

cv2.imshow('Paint', paint)

cv2.waitKey(0)
