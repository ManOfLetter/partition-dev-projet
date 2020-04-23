import cv2
import numpy as np 

forms = np.zeros((320,320,3), np.uint8)
forms = cv2.line(forms,(0,100),(300,100),(255,0,0),3) #(image)(coordonnée de départ)(coordonnée de fin)(couleur en RGB)(épaisseur)
forms = cv2.line(forms,(0,200),(300,200),(0,255,0),3) #(image)(coordonnée de départ)(coordonnée de fin)(couleur en RGB)(épaisseur)
forms = cv2.line(forms,(0,300),(300,300),(0,0,100),3) #(image)(coordonnée de départ)(coordonnée de fin)(couleur en RGB)(épaisseur)

cv2.imwrite('lines.png',forms)
cv2.waitKey(0)
cv2.destroyAllWindows()
