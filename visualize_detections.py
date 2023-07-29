# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from calculate_dimensions import calculate_dimensions
from matplotlib_imshow import matplotlib_imshow


# -----------------------------------------------------------------------------------------------
###                                      Visualize Detections                                ###
# -----------------------------------------------------------------------------------------------
def visualize_detections(src, pts):
    """
    src: image on which to draw the rotated rectangle and display the calculated width and height.
         should be BGR type image.
    pts: points array that outlines the object (to call the calculate_dimensions() function)

    Returns the modified image (BGR type).
    """
    src = src.copy()
    box2d_obj, (w, h) = calculate_dimensions(pts)
    corner_points = cv.boxPoints(box2d_obj).astype(np.int32)
    cv.polylines(src, [corner_points], isClosed=True, color=(0, 0, 255), thickness=1)
    cv.putText(
        src,
        f"Width: {round(w/10, 1)} cm",
        (10, 25),
        cv.FONT_HERSHEY_SCRIPT_SIMPLEX,
        0.5,
        (0, 0, 0),
        1,
    )
    cv.putText(
        src,
        f"Height: {round(h/10, 1)} cm",
        (10, 50),
        cv.FONT_HERSHEY_SCRIPT_SIMPLEX,
        0.5,
        (0, 0, 0),
        1,
    )

    return src
