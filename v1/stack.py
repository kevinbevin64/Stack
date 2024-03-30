"""
I realized when stacking 333 4.5MP images
that it would take 4.85 years to finish stacking on my computer...
Time to try C++!
"""

import math
from PIL import Image
import os
from math import floor

def listify(dir_name):
    image_filenames = []
    directory = os.listdir(dir_name)

    for filename in directory: 
        if os.path.isfile(dir_name + "/" + filename):
            if filename[-3:].lower() == "png" or filename[-3:].lower() == "jpg": 
                image_filenames.append(dir_name + "/" + filename)

    print("Found " + str(len(image_filenames)) + " image filenames!")

    return image_filenames

def stack(image_filenames):
    image_dimensions = Image.open(image_filenames[0]).size
    output_image = Image.new(mode="RGB", size=image_dimensions)

    for r in range(image_dimensions[0]):
        for c in range(image_dimensions[1]):
            print("Working on row " + str(r) + " column " + str(c))
            output_image.putpixel((r, c), average(image_filenames, r, c))

    output_image.show()


def average(image_filenames, row, column):
    r = 0
    g = 0
    b = 0

    last_percent = -1

    for i in range(len(image_filenames)):
        rgb_val = Image.open(image_filenames[i]).getpixel((row, column))
        r += rgb_val[0]
        g += rgb_val[1]
        b += rgb_val[2]

        if last_percent != floor(i * 100 / len(image_filenames)):
            last_percent = floor(i * 100 / len(image_filenames))
            print("\tSubtask " + str(last_percent) + "%" + " complete")

    r /= len(image_filenames)
    g /= len(image_filenames)
    b /= len(image_filenames)

    return  (int(r), int(g), int(b))

def main():
    # open all images and put them into a list
    # for each pixel of final image
    # go through all images
    # and average the rgb values for that pixel's location

    stack(listify("image"))

if __name__ == "__main__":
    main()
