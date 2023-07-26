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
    threshold_val, thresholded_img = cv.threshold(
        grayscale_img_blurred, 170, 255, cv.THRESH_BINARY, 5
    )
    return thresholded_img
