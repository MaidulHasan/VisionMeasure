# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------------------------
###                                      Perspective Transform                              ###
# -----------------------------------------------------------------------------------------------
def perspective_transform(source_img, actual_points, scale=4, pad=30):
    """
    source_img: image to transform (you shold pass in the original RGB image as it can be manipulated later).

    actual_points: 4 points on the source image (3 of which mustn't be colinear). Must be in the
    (top left, top right, bottom left, bottom right) order.

    scale: the image is by default transformed to an image of, w = (210 * scale) and h = (297 * scale).
    The to be points for perspective transformation is calculated from these w and h values. default is 4.

    pad: to apply padding to the perspective transformed image (to skip padding set, pad=0)

    Returns: a tuple of (scale, Padded perspective transformed image).
    """
    w = scale * 210
    h = scale * 297

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

    return (scale, padded_perspective_transformed_image)
