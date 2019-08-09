import matplotlib.pyplot as plt
import numpy as np
import cv2


def visualize(image, label):
    image = image.squeeze()
    # plt.clf()
    plt.figure(figsize=(8, 6))
    plt.imshow(image)
    plt.title(label)
    plt.show()


def to_argmax(string):
    word_list = "2345678abcdefghkmnprwxy"
    encoded = []
    try:
        for s in string:
            i = word_list.index(s)
            encoded.append(i)
    except ValueError:
        print("Error in string content:", string)
    finally:
        return np.array(encoded)


def argmax_to_string(encoded):
    word_list = "2345678abcdefghkmnprwxy"
    string = ""
    for i in encoded:
        string += word_list[i]
    return string

# Just include a bunch of functions here to preprocess stuff


# This function retrieves black lines in images.
def getline(images):
    # print(images.shape)
    return np.squeeze(np.dot(images[:, :, :], [[0.2989], [0.5870], [0.1140]]))


# This function locates and removes black line in image.
def subtract_image(image, line_image):  # image: (50, 200, 3), line_image: (50, 200)
    THRESHOLD = 25
    if image.shape[:2] != line_image.shape[:2]:
        raise ValueError("Dimension Error! image and line_image have different dimensions!")
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if line_image[i][j] < THRESHOLD:
                image[i][j].fill(255)
    return image


# This function reduce the line in the image and return image with line removed.
# This function calls getline() and subtract_image() to help finish the task.
def preprocess(images):
    kernel = np.ones((2, 1), np.uint8)
    processed_images = []
    for image in images:
        # Remove the black line in the picture.
        reduced_image = subtract_image(image.squeeze(), getline(image.squeeze()))

        # Do some transformations
        reduced_image = cv2.dilate(reduced_image, kernel, iterations=1)
        reduced_image = cv2.erode(reduced_image, kernel, iterations=2)

        # Convert from RGB to gray.
        reduced_image = cv2.cvtColor(reduced_image, cv2.COLOR_RGB2GRAY)
        reduced_image = cv2.threshold(reduced_image, 250, 255, cv2.THRESH_BINARY_INV)[1]

        # Resize the image.
        reduced_image = cv2.resize(reduced_image, (128, 32))
        processed_images.append([reduced_image])
    return np.array(processed_images)
