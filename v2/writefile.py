from PIL import Image
import os

def main():
    # define directory containing the images
    image_dir_str = "../images/dumbbells"
    image_dir = os.listdir(image_dir_str)
    filenames = []

    # find all image files
    for filename in image_dir: 
        if os.path.isfile(image_dir_str + "/" + filename):
            if (filename[-3:].lower() == "png" or filename[-3:].lower() == "jpg"):
                filenames.append(image_dir_str + "/" + filename)
    print(f"{len(filenames)} images found!")

    # write to stack.in file
    x_size = Image.open(filenames[0]).size[0]
    y_size = Image.open(filenames[0]).size[1]

    data_file = open("stack.in", "a")
    data_file.write(str(len(filenames)) + " ")
    data_file.write(str(x_size) + " ") # number of columns
    data_file.write(str(y_size) + "\n") # number of rows


    print("Writing images... ", end="")
    for i in range(len(filenames)):
        print(f"\rWriting images...({i + 1}/{len(filenames)})\t", end="")
        image = Image.open(filenames[i])
        for r in range(y_size):
            for c in range(x_size):
                pixel = image.getpixel((c, r))

                data_file.write(str(pixel[0]) + " ")
                data_file.write(str(pixel[1]) + " ")
                data_file.write(str(pixel[2]) + " ")

        data_file.write("\n")
    print("Done!")

if __name__ == "__main__":
    main()