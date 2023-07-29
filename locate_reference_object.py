# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from reorder_corner_points import reorder


# -----------------------------------------------------------------------------------------------
###              Find Contours and Filter out the Reference Object (A4 Paper)               ###
# -----------------------------------------------------------------------------------------------


def contour_perimeter(cnt):
    return cv.arcLength(cnt, closed=True)


def find_corners(preprocessed_img):
    """
    The input should be a processed binary 8 bit image.
    Returns the 4 corner points of the A4 paper in (top_left, top_right, bottom_left, bottom_right)
    order as an array of shape (4, 2) and dtype=np.float32
    """

    cnts, _ = cv.findContours(
        preprocessed_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
    )
    # find the contour with the largest perimeter
    ref_obj_cnt = sorted(cnts, key=contour_perimeter, reverse=True)[:1][0]
    # find the corners
    # output will be of shape (4, 1, 2).
    # keep it like that if you are to draw bounding box with cv.polylines
    corners = cv.convexHull(
        cv.approxPolyDP(ref_obj_cnt, 0.01 * contour_perimeter(ref_obj_cnt), closed=True)
    )
    if corners.shape[0] != 4:
        print("Couldn't detect reference object (A4 Paper).\n")
        print("You can try the following to make your image more recognizable : \n")
        print(
            """\t 1. Capture the image in a cleaner background. \n\t 
            2. Try to fit the whole A4 paper inside the frame. \n\t 
            3. Or, try again with different image.\n"""
        )
        return None
    else:
        reordered_corner_points = reorder(corners)
        if reordered_corner_points.flatten().all():
            return reordered_corner_points
        else:
            print("Please try to fit the whole A4 paper inside the frame.")
            return None
