# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------------------------
###              Find Contours and Filter out the Reference Object (A4 Paper)               ###
# -----------------------------------------------------------------------------------------------


def contour_perimeter(cnt):
    return cv.arcLength(cnt, closed=True)


def find_ref_object_corners(preprocessed_img):
    """
    The input should be a processed binary 8 bit image.
    Returns the 4 corner points of the A4 paper.
    In counter-clockwise direction starting from top right corner, 
    i.e, top right, top left, bottom left and bottom right
    """

    cnts, hier = cv.findContours(
        preprocessed_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
    )
    # find the contour with the largest perimeter
    ref_obj_cnt = sorted(cnts, key=contour_perimeter, reverse=True)[:1][0]
    # find the corners (output will be of shape (4, 1, 2). keep that.)
    corners = cv.approxPolyDP(
        ref_obj_cnt, 0.01 * contour_perimeter(ref_obj_cnt), closed=True
    )
    return corners


# -----------------------------------------------------------------------------------------------
###                                      Perspective Transform                              ###
# -----------------------------------------------------------------------------------------------
