import cv2
from static import model

def convert_to_grayscale(image):
    """
    Converts the input image to grayscale.

    Parameters:
    image (numpy array): Input image.

    Returns:
    numpy array: Grayscale image.
    """
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

def resize_image(image, size=(48, 48)):
    """
    Resizes the input image to the specified size.

    Parameters:
    image (numpy array): Input image.
    size (tuple): Desired size (width, height). Default is (48, 48).

    Returns:
    numpy array: Resized image.
    """
    resized_image = cv2.resize(image, size, interpolation=cv2.INTER_AREA)
    return resized_image


def get_prediction(finalimg):
    prediction = model.keras.predict(finalimg)
    return prediction
