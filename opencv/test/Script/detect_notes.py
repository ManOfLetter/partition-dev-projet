import numpy as np
import sys
import cv2 as cv


def show_wait_destroy(winname, img):
    cv.imshow(winname, img)
    cv.moveWindow(winname, 500, 0)
    cv.waitKey(0)
    cv.destroyWindow(winname)


def main(argv):
    
    #Partie 1

    # Chargement de l'image
    src = cv.imread("Images/notes.png", cv.IMREAD_COLOR)

    # [gray]
    # Transformation de l'image de base en nuance de gris
    if len(src.shape) != 2:
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    else:
        gray = src


    # [bin]
    # On applique l'inversion de couleur
    gray = cv.bitwise_not(gray)
    bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, -2)
    # [bin]

    # [init]
    # On va crée l'image qui va être utilisé pour extraire les lignes verticales
    vertical = np.copy(bw)
    # [init]

    # [vert]
    # On spécifie la taille sur l'axe y (ici shape[0] represente les colonnes)
    rows = vertical.shape[0]
    verticalsize = rows // 30

    # Création d'une structure pour l'extraction des lignes verticales à l'aide des opération morphologiques
    verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))

    # Apply morphology operations
    vertical = cv.erode(vertical, verticalStructure)
    vertical = cv.dilate(vertical, verticalStructure)


    # [smooth] - on vient appliquer des transformation à l'image afin de récupérer son contour et la remplir à nouveau
    # On inverse l'image à  nouveau
    vertical = cv.bitwise_not(vertical)

    # Etape 1
    edges = cv.adaptiveThreshold(vertical, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, -2)
    show_wait_destroy("edges", edges)

    # Etape 2
    kernel = np.ones((2, 2), np.uint8)
    edges = cv.dilate(edges, kernel)
    show_wait_destroy("dilate", edges)

    # Etape 3
    smooth = np.copy(vertical)

    # Etape 4
    smooth = cv.blur(smooth, (2, 2))

    # Etape 5
    (rows, cols) = np.where(edges != 0)
    vertical[rows, cols] = smooth[rows, cols]

    # On montre et on enregistre le resultat final dans le dossier de travail
    show_wait_destroy("smooth - final", vertical)
    cv.imwrite("vertical.png",vertical)
    # [smooth]

    #Partie 2
    image = cv.imread('vertical.png')

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY) #On transforme l'image en nuance de gris
    ret,thresh = cv.threshold(gray,250,255,cv.THRESH_BINARY_INV)

    img,contours,h =cv.findContours(thresh,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE) #On va chercher les contours des formes présente sur l'image.

    for cnt in contours:
        perimetre=cv.arcLength(cnt,True)
        approx = cv.approxPolyDP(cnt,0.01*perimetre,True)
        M = cv.moments(cnt)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv.drawContours(image,[cnt],-1,(0,255,0),2)
        
        if len(approx)==3:
            shape = "triangle"
        elif len(approx)==4:
            (x, y, w, h) = cv.boundingRect(approx)
            ratio = w / float(h)
            if ratio >= 0.95 and ratio <= 1.05:
                shape = "carre"
            else:
                shape = "rectangle"
        elif len(approx)==5:
            shape = "pentagone"
        elif len(approx)==6:
            shape = "hexagone"
        else:
            shape= "notes"
        cv.putText(image, shape, (cX, cY), cv.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 1)


    cv.imwrite('test_noire.jpg', image)
    cv.imshow('image',image)
    cv.waitKey(0)
    
    return 0 

if __name__ == "__main__":
    main(sys.argv[1:])
