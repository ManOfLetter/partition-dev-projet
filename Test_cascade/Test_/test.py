import cv2
cle_cascade = cv2.CascadeClassifier('cascade.xml')
img = cv2.imread('partition.jpeg')
clesol = cle_cascade.detectMultiScale(img, scaleFactor=1.022, minNeighbors=5)
for (x,y,w,h) in clesol:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
