# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import numpy as np


# -----------------------------------------------------------------------------------------------
### Reorder corner points of a rectangle in top left, top right, bottom left, bottom right order ###
# -----------------------------------------------------------------------------------------------
def reorder(rectangle_corner_points):
    """
    Reorder corner points of a rectangle in top left, top right, bottom left, bottom right order.

    Returns the corners as a (4, 2) array of datatype=np.float32
    """

    rectangle_corner_points = rectangle_corner_points.reshape(4, 2)

    # if we sum up the x and y values of the coordinates,
    # the least one will be top_left and the greatest one will be bottom_right
    # let, top_right = (x2, y2) and bottom_left = (x3, y3)
    # now, x3 < x2 and y3 > y2
    # thus, (y3 - x3) > (y2-x2)
    # so, we remove the two entries found beforehand i.e, top_left and bottom_right
    # and then find the difference between the y and x values of the coordinates
    # the least one will be top_right and the greatest one will be bottom_left

    sum_of_corner_x_and_y_coordinate_values = np.sum(rectangle_corner_points, axis=1)
    top_left_idx = np.argmin(sum_of_corner_x_and_y_coordinate_values)
    bottom_right_idx = np.argmax(sum_of_corner_x_and_y_coordinate_values)
    temp_corners = np.delete(
        rectangle_corner_points.copy(), [top_left_idx, bottom_right_idx], axis=0
    )
    diff_of_temp_corners = np.diff(temp_corners, axis=1)
    top_right_idx = np.argmin(diff_of_temp_corners)
    bottom_left_idx = np.argmax(diff_of_temp_corners)

    top_left = rectangle_corner_points[top_left_idx]
    top_right = temp_corners[top_right_idx]
    bottom_left = temp_corners[bottom_left_idx]
    bottom_right = rectangle_corner_points[bottom_right_idx]

    return np.array([top_left, top_right, bottom_left, bottom_right]).astype(np.float32)
