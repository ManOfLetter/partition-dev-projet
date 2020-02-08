import cv2
import numpy as np

image = cv2.imread('MadWorld.jpg')
image2 = cv2.imread('Lune.jpg')
image_chopin = cv2.imread('chopin.png')

ligne = 0

#image[100:200, 100:200] = (255,0,0)

for i in range(100,270):
    (b, g, r) = image[i,500]
    (b2, g2, r2) = image[i-1,500]

    if (b<200 and g<200 and r<200):

        if (b2>100 and g2>100 and r2>100):
            (b3, g3, r3) = image[i,550]

            if (b3<200 and g3<200 and r3<200):
                ligne=ligne+1
                print (b,g,r) # on affiche les 3 intensites representant notre couleur
        #else:
            #print (b2,g2,r2)
    
    image[i-1,500] = (0,255,255) # le pixel [i,j] change de couleur

print ("Nombre de lignes = ", ligne)

cv2.imshow("Partition", image) # creation d'une fenetre appelee Partition contenant image

cv2.waitKey(0) # detruire la fenetre après pression d'une touche