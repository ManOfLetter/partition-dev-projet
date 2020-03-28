"""
@file morph_lines_detection.py
@brief Use morphology transformations for extracting horizontal and vertical lines sample code
"""
import numpy as np
import sys
import cv2 as cv


def show_wait_destroy(winname, img):
    cv.imshow(winname, img)
    cv.moveWindow(winname, 500, 0)
    cv.waitKey(0)
    cv.destroyWindow(winname)


def main(argv):

    # Load the image
    src = cv.imread("notes.png", cv.IMREAD_COLOR)

    # Show source image
    cv.imshow("src", src)
    # [load_image]

    # [gray]
    # Transform source image to gray if it is not already
    if len(src.shape) != 2:
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    else:
        gray = src

    # Show gray image
    show_wait_destroy("gray", gray)
    # [gray]

    # [bin]
    # Apply adaptiveThreshold at the bitwise_not of gray, notice the ~ symbol
    gray = cv.bitwise_not(gray)
    bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 15, -2)
    # Show binary image
    show_wait_destroy("binary", bw)
    # [bin]

    # [init]
    # Create the images that will use to extract the horizontal and vertical lines
    horizontal = np.copy(bw)
    vertical = np.copy(bw)
    # [init]

    # [horiz]
    # Specify size on horizontal axis
    cols = horizontal.shape[1]
    horizontal_size = cols // 30

    # Create structure element for extracting horizontal lines through morphology operations
    horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT, (horizontal_size, 1))

    # Apply morphology operations
    horizontal = cv.erode(horizontal, horizontalStructure)
    #horizontal = cv.dilate(horizontal, horizontalStructure)

    # Show extracted horizontal lines
    show_wait_destroy("horizontal", horizontal)
    # [horiz]

       
    # [vert]
    # Specify size on vertical axis
    rows = vertical.shape[0]
    verticalsize = rows // 30

    # Create structure element for extracting vertical lines through morphology operations
    verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))

    # Apply morphology operations
    vertical = cv.erode(vertical, verticalStructure)
    vertical = cv.dilate(vertical, verticalStructure)

    # Show extracted vertical lines
    show_wait_destroy("vertical", vertical)
    # [vert]

    # [smooth]
    # Inverse vertical image
    vertical = cv.bitwise_not(vertical)
    show_wait_destroy("vertical_bit", vertical)

    '''
    Extract edges and smooth image according to the logic
    1. extract edges
    2. dilate(edges)
    3. src.copyTo(smooth)
    4. blur smooth img
    5. smooth.copyTo(src, edges)
    '''

    # Step 1
    edges = cv.adaptiveThreshold(vertical, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, -2)
    show_wait_destroy("edges", edges)

    # Step 2
    kernel = np.ones((2, 2), np.uint8)
    edges = cv.dilate(edges, kernel)
    show_wait_destroy("dilate", edges)

    # Step 3
    smooth = np.copy(vertical)

    # Step 4
    smooth = cv.blur(smooth, (2, 2))

    # Step 5
    (rows, cols) = np.where(edges != 0)
    vertical[rows, cols] = smooth[rows, cols]

    # Show final result
    show_wait_destroy("smooth - final", vertical)
    cv.imwrite("vertical.png",vertical)
    # [smooth]

    image = cv.imread('vertical.png')

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret,thresh = cv.threshold(gray,250,255,cv.THRESH_BINARY_INV)

    img,contours,h =cv.findContours(thresh,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

    decal = 0
    for cnt in contours:
        perimetre=cv.arcLength(cnt,True)
        approx = cv.approxPolyDP(cnt,0.01*perimetre,True)
        decal = decal + 10 
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
        #cv.putText(image, shape, (cX, 120+decal), cv.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 1)
        cv.putText(image, shape, (cX, cY), cv.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 1)


    cv.imwrite('test_noire.jpg', image)
    cv.imshow('image',image)
    cv.waitKey(0)
    
    return 0 

if __name__ == "__main__":
    main(sys.argv[1:])


