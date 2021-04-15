import cv2
import numpy as np

#dim = (640, 480)
image1 = cv2.imread('images/img1.jpg',cv2.IMREAD_COLOR)
image1_f = cv2.resize(image1, (0,0), None, 0.2,0.2)
image2 = cv2.imread('images/img2.jpg', cv2.IMREAD_COLOR)
image2_f = cv2.resize(image2, (0,0), None, 0.2,0.2)
#image3 = cv2.imread('images/i3.jpg', cv2.IMREAD_COLOR)
#image3_f = cv2.resize(image3, (0,0), None, 0.2,0.2)
#cv2.imshow('Left', image1_f)
#cv2.imshow('Right', image2_f)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


pictures = []
pictures.append(image1_f)
pictures.append(image2_f)
#pictures.append(image3_f)

stitcher = cv2.Stitcher.create()
ret, pano = stitcher.stitch(pictures)

if ret == cv2.Stitcher_OK:
    cv2.imshow("Panorama", pano)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Error during stitching.')







