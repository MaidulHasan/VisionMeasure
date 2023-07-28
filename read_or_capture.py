# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from imutils import rotate_bound


# -----------------------------------------------------------------------------------------------
###                                         Read Image                                      ###
# -----------------------------------------------------------------------------------------------


def read_image(img_path):
    try:
        img = cv.imread(img_path)
        return img
    except:
        print("Invalid Image Path")


# -----------------------------------------------------------------------------------------------
###                                         Capture Live Image                              ###
# -----------------------------------------------------------------------------------------------
def take_picture(device_id=0):
    cap = cv.VideoCapture(device_id)

    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 700)

    try:
        if cap.isOpened() is False:
            cap.open()
    except:
        print("Maybe try with another device. Exiting...\n")
        return None

    while True:
        ret, frame = cap.read()

        if ret is False:
            print("Could not read any frame. Exiting.... \n")
            break

        cv.imshow("To capture an image, press 'c' and to quit, press 'q'", frame)

        key_pressed = cv.waitKey(1)  # wait 1 mili second for key press

        if key_pressed == ord("c"):
            captured_image = frame
            break
        if key_pressed == ord("q"):
            captured_image = None
            print("No image was captured. Quitting..... \n")
            break

    cap.release()
    cv.destroyAllWindows()

    return captured_image


# -----------------------------------------------------------------------------------------------
###                                         User Input                                      ###
# -----------------------------------------------------------------------------------------------


def usr_prompt():
    """
    Prompt the user to provide a valid image path or a valid device id to capture one.

    Returns: User input
    """
    try:
        img_path_or_capture = int(
            input(
                "Please select \n 1. to provide an image path or, 2. to take a live picture \n (1, 2): \t"
            )
        )
    except:
        raise

    print(f"img_path_or_capture: {img_path_or_capture}")

    if img_path_or_capture not in [1, 2]:
        print("Invalid input. Please choose either 1 or 2.")

    if img_path_or_capture == 1:
        img_path = input("Please provide a valid image path : \t")
        return img_path

    if img_path_or_capture == 2:
        video_capture_device_id = input(
            "Please provide a device id (to capture the image with, default is 0): \t"
        )

        if video_capture_device_id == "":
            video_capture_device_id = 0

        try:
            video_capture_device_id = int(video_capture_device_id)
            return video_capture_device_id

        except:
            raise


# -----------------------------------------------------------------------------------------------
###                                     Read or Capture Image                               ###
# -----------------------------------------------------------------------------------------------


def read_or_capture(prompt_usr=True, img_path=None, device_id=None):
    if prompt_usr:
        usr_input = usr_prompt()

        if type(usr_input) == str:
            img = read_image(usr_input)

        if type(usr_input) == int:
            img = take_picture(usr_input)

            if img is None:
                print("Please capture another image or provide a valid image path. \n")
                return None

    if not prompt_usr and img_path:
        img = read_image(img_path)

    if not prompt_usr and device_id is not None:
        img = take_picture(device_id)

        if img is None:
            print("Please capture another image or provide a valid image path. \n")
            return None

    # rotate the image by 90 degree CCW if image width > image height
    if img.shape[0] < img.shape[1]:
        img = rotate_bound(img, -90)

    return img
