--------------------------------------------------
# VisionMeasure: Object Dimesion Measurement with OpenCV
----------------------------------------------

----------------------------------------
## Project Goal

The goal is to develop a system using OpenCV that can be used to reliably measure the dimension of various types of objects in real time using the presence of a known object (object whose dimension is known) in the frame. 

-----------------------------------------------

## Current Status, Usage and Project Description

The object to measure should be placed in an A4 paper whose dimensions are known (210 x 297 mm). 

### Caution !!!
Before you proceed to use this application please note the following -- 
    1. Since the A4 paper is white, placing white objects on the paper will 
    most likely produce faulty outcome.
    2. Place only one object on the A4 paper at a time. To reduce false detection, only the highest 
    perimeter object is filtered from all the possible detections.
    3. This application only uses OpenCV and no deep learning model. So, due 
    to constraints of classical computer vision the results may not be 
    100% accurate. Long story short, Use at your own risk.

To improve the chance of correct recognition and measurement you can do the following --
    1. Capture the image in a clean background.
    2. Try to fit the whole A4 paper inside the frame.
    3. Lighting condition should not be too dark or too bright.

### Usage
Current implementation has a python script named "`pipeline_for_still_images.py`" which is a pipeline for detecting objects of interest from a still image and find the objects dimensions (width, height) in cm.

*Object of interest - Largest perimeter object placed on top of the A4 paper.

**Args**:
    prompt_user: whether to prompt the user for image path or, device id. (default: False)
    image_path: to use a stock/pre-captured image instead of prompting the user. (default: "./sample_imgs/paint_brush.jpeg")
    capturing_device_id: to capture a live image instead of prompting or loading a stock one. (default: None)
    visualize: whether to show the output image containing the info of detections. (default: True)
    scale: matplotlib_imshow() function visualization scale. (default: 8)

**Returns**: The output image (A rotated bounding box is drawn around the object of interest. The calculated dimensions (width, height) are also shown on the output image.)

-------------------------------------------------

## Future Prospect

1. **Real time detection**: measurement from live capture (currently I don't have any USB Webcam so couldn't implement right now).
2. **Dimension Verification**: a validation step can be introduced to ensure the accuracy of the measured dimensions. This could involve comparing the measured dimensions to ground-truth values or using multiple reference objects for calibration.
3. **Use a reference object of the users choosing**. 
4. **User Interface (Optional)**: a simple graphical user interface (GUI) to input images or videos, display the results, and provide some options for customization.

-----------------------------------------------------