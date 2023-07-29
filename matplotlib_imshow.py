# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------------------------
###                                      Matplotlib Imshow                                 ###
# -----------------------------------------------------------------------------------------------


# converting color mode to RGB and displaying the image as matplotlib figure
def matplotlib_imshow(
    img_title="", img=None, scale=5, cv_colorspace_conversion_flag=cv.COLOR_BGR2RGB
):
    """
    title: plot title (to be shown)
    img: image to plot
    scale = 5: the default scaling is 5
    cv_colorspace_conversion_flag = cv.COLOR_BGR2RGB: colorspace conversion
    """

    # tinkering with size
    try:
        img_height, img_width = img.shape[0], img.shape[1]
        aspect_ratio = img_width / img_height
        plt.figure(figsize=(scale, scale * aspect_ratio))
    except AttributeError:
        print(
            "None Type image. Correct_syntax is, matplotlib_imshow(img_title, img, fig_h, cv_colorspace_conversion_flag)."
        )

    # actual code for displaying the image
    plt.imshow(cv.cvtColor(img, cv_colorspace_conversion_flag))
    plt.title(img_title)
    plt.show()
