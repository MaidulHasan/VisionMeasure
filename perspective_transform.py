# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------------------------
###                                      Perspective Transform                              ###
# -----------------------------------------------------------------------------------------------
def perspective_transform(source_img, actual_points, pad=5):
    """
    source_img: image to transform (you shold pass in the original RGB image as it can be manipulated later).

    actual_points: 4 points on the source image (3 of which mustn't be colinear). Must be in the
    (top left, top right, bottom left, bottom right) order.

    pad: to apply padding to the perspective transformed image (to skip padding set, pad=0)

    Returns: perspective transformed image of shape (210, 297) [note: this shape is without padding].
    """
    w = 210
    h = 297

    to_be_points = np.array([[0, 0], [w, 0], [0, h], [w, h]], dtype=np.float32)

    perspective_transform_matrix = cv.getPerspectiveTransform(
        actual_points, to_be_points
    )
    perspective_transformed_img = cv.warpPerspective(
        source_img, perspective_transform_matrix, (w, h)
    )

    # apply padding

    padded_perspective_transformed_image = perspective_transformed_img[
        pad : h - pad, pad : w - pad
    ]

    return padded_perspective_transformed_image
