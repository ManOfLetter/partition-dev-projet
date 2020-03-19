import cv2
import numpy

image = numpy.zeros((100,100,3), dtype='uint8') #creation de mon image vide

cv2.rectangle(image, (0,0), (100,100), (255,255,255), 100) 

cv2.line(image, (0,50), (100,50), (0,0,0), 2) #on dessine une droite

cv2.line(image, (0,25), (100,25), (0,0,0), 2) #on dessine une droite

cv2.line(image, (0,75), (100,75), (0,0,0), 2) #on dessine une droite

cv2.imshow("test", image) 
cv2.imwrite('test_lines.jpg', image)
cv2.waitKey(0)
