import math
from PIL import Image
import os

def listify(dir_name):
    image_filenames = []
    directory = os.listdir(dir_name)

    for filename in directory: 
        if os.path.isfile(dir_name + "/" + filename):
            if filename[-3:] == "png" or filename[-3:] == "jpg": 
                image_filenames.append(dir_name + "/" + filename)

    image_list = []
    for filename in image_filenames:
        image_list.append(Image.load(filename).load())

    return image_list

def mean(pixel_vals):
    total = 0;
    for value in pixel_vals:
        total += value;
    return total / len(pixel_vals)

def main():
    # open all images and put them into a list
    # for each pixel of final image
    # go through all images
    # and average the rgb values for that pixel's location

    listify("images")

if __name__ == "__main__":
    main()
