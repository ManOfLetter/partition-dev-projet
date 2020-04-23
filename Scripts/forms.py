import numpy as np
import cv2

forms = np.zeros((512,512,3), np.uint8)
forms = cv2.line(forms,(0,0),(511,511),(255,0,0),5) #(image)(coordonnée de départ)(coordonnée de fin)(couleur en RGB)(épaisseur)
forms = cv2.rectangle(forms,(384,0),(510,128),(0,255,0),3) #(image)(coordonnée coin en haut à gauche)(coordonnée coin en bas à droite)(couleur en RGB)(épaisseur)
forms = cv2.circle(forms,(447,63), 63, (0,0,255), -1) #(image)(coordonnée centre)(radius)(couleur en RGB)(épaisseur, -1 pour remplir)
forms = cv2.ellipse(forms,(256,256),(50,50),180,0,270,(255,255,0),50) #(image)(coordonnée centre)(radius)(couleur en RGB)(épaisseur, -1 pour remplir)


pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32) 
pts = pts.reshape((-1,1,2))
forms = cv2.polylines(forms,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(forms,'Etienne',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('image',forms)
cv2.waitKey(0)
cv2.destroyAllWindows()

