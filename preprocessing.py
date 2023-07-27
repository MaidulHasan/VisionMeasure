# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from imutils import rotate_bound


# -----------------------------------------------------------------------------------------------
###                                         Image Preprocessing                             ###
# -----------------------------------------------------------------------------------------------
def preprocess(img):
    # rotate the image by 90 degree CCW if image width > image height
    if img.shape[0] < img.shape[1]:
        img = rotate_bound(img, -90)

    grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    grayscale_img_blurred = cv.GaussianBlur(grayscale_img, (5, 5), 0, 0)

    # By experimenting we've found, threshold = 130 works best for a wide range of image backgrounds
    _, thresholded_img = cv.threshold(grayscale_img_blurred, 130, 255, cv.THRESH_BINARY)

    # Erosion to detach any contour that remains loosely connected to the A4 paper contour
    morph_operation_kernel = np.ones(
        (3, 3), dtype=np.uint8
    )  # same as MORPH_RECT of size 3
    thresholded_img_eroded = cv.erode(
        thresholded_img, morph_operation_kernel, iterations=2
    )

    preprocessed_img = thresholded_img_eroded
    return preprocessed_img
