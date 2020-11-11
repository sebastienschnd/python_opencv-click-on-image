import cv2
import numpy as np

def mousePoints(event, x, y, flags, params):
    if event = cv2.EVENT_LBUTTONDOWN:
        print(x, y)

img = cv2.imread('Resources/cards0.jpg')

width, height = 250, 350
pts1 = np.float32([[111, 210], [287, 188], [154, 482], [352, 4440]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

for x in range (0,4)
    cv2.circle(img,(pts1[x][0], pts1[x][1]), 15, (0, 255, 0), cv2.FILLED)

cv2.imshow("Original Image", img)
cv2.setMouseCallBack("Original Image", MousePoints) 
#cv2.imshow("Output image ", imgOutput)
cv2.waitKey(0)

