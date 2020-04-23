import cv2
import numpy as np
import imutils

"""
Ici j'importe mon image, je la passe en noir et blanc, je la floute,
puis j'applique mon filtre de Canny automatique.
Je cree mon mask de la meme dimension que mon image

Ensuite je cherche les contours et je les stock dans "cnts" qui est une liste contenant
les contours.

Ensuite je parcours cette liste et si l'aire du contour est superieur a 80 alors
je considere que c'est une piece donc je la dessine sur mon mask et j'augmente le compteur de 1.

Une fois que tous les contours sont passes. J'ecris le nombre de pieces trouvees et
je masque mon image de base

J'affiche ensuite le resultat
"""
image = cv2.imread('piecetest.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
flougaussien = cv2.GaussianBlur(gray, (3,3), 0)
#flougaussien = cv2.bilateralFilter(gray, 5, 40, 40)
edge = imutils.auto_canny(flougaussien)
mask = np.zeros(image.shape[:2], dtype='uint8')

(cnts, _) = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
compteur = 0

for c in cnts:
    if (cv2.contourArea(c) > 80):

        cv2.drawContours(mask, [c], 0, (255,255,255),-1)
        compteur += 1


resultat = cv2.bitwise_and(image, image, mask = mask)

text = " {} pieces trouvees".format(compteur)
cv2.putText(resultat, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,0), 2)

cv2.imshow("resultat", resultat)

cv2.waitKey(0)
