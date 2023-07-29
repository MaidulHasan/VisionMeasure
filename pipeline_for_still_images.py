# -----------------------------------------------------------------------------------------------
###                                         Imports                                         ###
# -----------------------------------------------------------------------------------------------

from matplotlib_imshow import matplotlib_imshow

from read_or_capture import read_or_capture
from preprocessing import preprocess
from locate_reference_object import find_corners
from perspective_transform import perspective_transform
from locate_object_of_interest import find_object_of_interest
from calculate_dimensions import calculate_dimensions
from visualize_detections import visualize_detections


# -----------------------------------------------------------------------------------------------
###         Pipeline for Detection, Measurement and Visualization (from still Images)       ###
# -----------------------------------------------------------------------------------------------


def pipeline_for_still_images(
    prompt_user=False,
    image_path="./sample_imgs/paint_brush.jpeg",
    capturing_device_id=None,
    visualize=True,
    scale=8,
):
    """
    A pipeline for detecting objects of interest from a still image and find the objects dimensions (width, height) in cm.

    Args:
        prompt_user: whether to prompt the user for image path or, device id. (default: False)
        image_path: to use a stock/pre-captured image instead of prompting the user. (default: "./sample_imgs/paint_brush.jpeg")
        capturing_device_id: to capture a live image instead of prompting or loading a stock one. (default: None)
        visualize: whether to show the output image containing the info of detections. (default: True)
        scale: matplotlib_imshow() function visualization scale. (default: 8)

    Returns: The output image (A rotated bounding box is drawn around the object of interest. The calculated dimensions (width, height) are also shown on the output image.)

    """

    # Read or capture an image
    img = read_or_capture(prompt_user, image_path, capturing_device_id)

    # Preprocessing for locating the reference object (A4 paper)
    preprocessed_img = preprocess(img)

    # Find the 4 corners of the reference object (A4 paper)
    corners = find_corners(preprocessed_img)

    # Perspective transformation of the original image
    perspective_transformed_img = perspective_transform(img, corners)

    # Find the set of points that defines the outline of the object of interest
    # Object of interest: Largest perimeter object placed on top of the A4 paper
    convex_hull = find_object_of_interest(perspective_transformed_img)

    # Output image to be shown
    # A rotated bounding box is drawn around the object of interest
    # The calculated dimensions (width, height) are also shown on the output image
    output_img_to_show = visualize_detections(perspective_transformed_img, convex_hull)

    if visualize is True:
        # Show the output image using the matplotlib_imshow() function with a scale of 10
        matplotlib_imshow(
            "Detected Object and its Calculated measurements \n(Width and Height) in cm",
            output_img_to_show,
            scale,
        )

    return output_img_to_show


if __name__ == "__main__":
    output_img = pipeline_for_still_images()
