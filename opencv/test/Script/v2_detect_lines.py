import numpy as np

import cv2 as cv

def main(argv):

    src = cv.imread('partition.jpeg', cv.IMREAD_COLOR)
    cv.imshow('Image originale', src)

    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    cv.imshow('Noir&Blanc', src)

    gray = cv.bitwise_not(gray)
    bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, -2)

    cv.imshow("binary", bw)

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])