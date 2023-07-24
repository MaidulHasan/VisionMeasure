-----------------------------------
# VisionMeasure: Object Dimesion Measurement with OpenCV
----------------------------------

## Project Goal

The goal is to develop a system using OpenCV that can be used to reliable measure the dimension of various types of objects in real time. For now, the object to measure should be placed in an A4 paper whose dimensions are known (210 x 297 mm). Later we intend to add functionality to upload a reference object of the users choosing. The output will be provided in real time.

## Project Outline

1. **Image Preprocessing**: 
    - Set video capture properties such as height and width to ensure each capture is consistent 
    - image blurring, denoising, adaptive thresholding to improve edge detection and contour extraction.

2. **Contour Filtering and Dimension Measurement**: 
    - Filter out the reference object in the image (whose dimension is known) 
    - Extract and Perspective transform the reference object.
    - Calculate dimension per pixel (known_height/height_in_pixel)
    - Filter relevant contours based on criteria like area, aspect ratio, or circularity
    - Fit a rotated rectangle (for circular objects you can fit circle too)
    - Find out the dimension of the object by multiplying the pixel information with the dimension per pixel measure found earlier
    - The calculation steps can be rpeated say for the frames in a 2s video capture and the result can be averaged for greater accuracy and resiliance to camera stability issues.

3. **Dimension Verification (Optional)**: 
    - A validation step can be introduced to ensure the accuracy of the measured dimensions. This could involve comparing the measured dimensions to ground-truth values or using multiple reference objects for calibration.

4. **Visualization and Output**: 
    - After measuring the dimensions for each frame in the video or the single image, generate a visual output i.e, drawing bounding boxes around the detected objects and displaying their measured dimensions.

5. **User Interface (Optional)**: 
    - a simple graphical user interface (GUI) to input images or videos, display the results, and provide options for customization.

## Project Status

Currently at step 1 (developing the image capturing and preprocessing pipeline).