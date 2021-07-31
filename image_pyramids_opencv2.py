import cv2
import numpy as np

img = cv2.imread('messi.jpg')
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)

ur1 = cv2.pyrUp(lr2)
ur2 = cv2.pyrUp(lr1)
ur3 = cv2.pyrUp(img)


cv2.imshow("Original image", img)
cv2.imshow("PyrDown 1 image", lr1)
cv2.imshow("PyrDown 2 image", lr2)
cv2.imshow("PyrUp 1 image", ur1)
cv2.imshow("PyrUp 2 image", ur2)
cv2.waitKey(0)
cv2.destroyAllWindows()