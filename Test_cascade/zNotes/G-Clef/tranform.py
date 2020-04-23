import cv2

img = cv2.imread('1.png',cv2.COLOR_BGR2GRAY)
cv2.imwrite('sol.png',img)

