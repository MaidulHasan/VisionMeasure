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


def find_object_of_interest(perspective_transformed_img):
    """
    The input should be the 3 channel BGR Perspective Transformed Image.
    Returns the Convex Hull of the Object of interest from top of
    the A4 paper in the Perspective Transformed Image.
    """

    # first we convert the BGR image to HSV color space since it's more suitable for
    # object detection based on color range

    h, s, v = cv.split(cv.cvtColor(perspective_transformed_img, cv.COLOR_BGR2HSV))

    # the 'h' channel has very erratic output
    # we blank it out and then merge the blank 'h_0' channel with the 's' and 'v' channels
    # operating only on the 's' channel may have been enough but we have seen that merging
    # the 's' and 'v' channels along with 'h_0' produces better result when thresholded

    h_0 = np.zeros_like(h)
    sv = cv.merge((h_0, s, v))
    _, thresh_sv = cv.threshold(
        cv.GaussianBlur(sv, (3, 3), 0, 0), np.mean(sv) / 2, 255, cv.THRESH_BINARY
    )

    # but we have to add these two more steps as the threshodled image is in "HSV" color space
    # but we need it to be grayscaled and then thresholded for contour detection
    # directly converting the 'sv' image to 'gray' and then thresholding
    # doesn't produce desired result

    sv_rgb = cv.cvtColor(thresh_sv, cv.COLOR_HSV2RGB)
    sv_gray = cv.cvtColor(sv_rgb, cv.COLOR_RGB2GRAY)
    _, thresh_img = cv.threshold(sv_gray, 220, 255, cv.THRESH_BINARY_INV)

    # we find the contours and then sort them by the perimeter in descending order
    cnts, _ = cv.findContours(thresh_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    # the largest perimeter contour is selected to reduce false detections
    obj_of_interest_cnt = sorted(cnts, key=contour_perimeter, reverse=True)[0]

    obj_of_interest_approx_cnt = cv.approxPolyDP(
        obj_of_interest_cnt, 0.005 * contour_perimeter(obj_of_interest_cnt), closed=True
    )
    obj_of_interest_chull = cv.convexHull(obj_of_interest_approx_cnt)

    return obj_of_interest_chull
