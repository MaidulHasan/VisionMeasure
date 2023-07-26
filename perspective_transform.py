# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------------------------
###                                      Perspective Transform                              ###
# -----------------------------------------------------------------------------------------------
def perspective_transform(source_img, actual_points, to_be_points, output_img_size):
    """
    source_img: image to transform
    actual_points: 4 points on the source image (3 of which mustn't be colinear).
    to_be_points: to be points in the output image
    output_img_size: should be a tuple

    Returns - Perspective transformed image.
    """

    perspective_transform_matrix = cv.getPerspectiveTransform(
        actual_points, to_be_points
    )
    return cv.warpPerspective(source_img, perspective_transform_matrix, output_img_size)
