# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------------------------
###                                      Calculate Dimensions                                ###
# -----------------------------------------------------------------------------------------------
def calculate_dimensions(pts):
    """
    Calculates the Width and Height of an object by fitting a Rotated Rectangle to a set of
    points (an array or points) that defines the outline of that object.

    Returns: Box2D_Obj, (Width, Height)
    """
    box2d_obj = cv.minAreaRect(pts)

    (cx, cy), (w, h), theta = box2d_obj

    return box2d_obj, (w, h)
