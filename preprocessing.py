# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------------------------
###                                         Image Preprocessing                             ###
# -----------------------------------------------------------------------------------------------
def preprocess(img):
    grayscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    grayscale_img_blurred = cv.GaussianBlur(grayscale_img, (5, 5), 0, 0)

    # C = 0 will produce an image that outlines the edges as white
    # Gaussian Kernel of size 3 works best (produces less white noise)
    # So first erosion to minimize white noise (more than 1 iteration will eliminate the edges)
    # Then dilation to widen the edges (2 or 3 iterations are enough)
    thresholded_img = cv.adaptiveThreshold(
        grayscale_img_blurred,
        255,
        cv.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv.THRESH_BINARY,
        3,
        0,
    )
    morph_operation_kernel = np.ones(
        (3, 3), dtype=np.uint8
    )  # same as MORPH_RECT of size 3
    thresholded_img_eroded = cv.erode(
        thresholded_img, morph_operation_kernel, iterations=1
    )
    eroded_img_dilated = cv.dilate(
        thresholded_img_eroded, morph_operation_kernel, iterations=3
    )

    preprocessed_img = eroded_img_dilated
    return preprocessed_img
