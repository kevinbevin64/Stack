from PIL import Image
import os

def main():
    dir_name = "../images/dumbbells"

    image_filenames = []
    directory = os.listdir(dir_name)

    for filename in directory: 
        if os.path.isfile(dir_name + "/" + filename):
            if filename[-3:].lower() == "png" or filename[-3:].lower() == "jpg": 
                image_filenames.append(dir_name + "/" + filename)

    print("Found " + str(len(image_filenames)) + " images!")

    written_file = open("stack.in", "a")

    c = Image.open(image_filenames[0]).size[0]
    r = Image.open(image_filenames[0]).size[1]

    written_file.write(str(len(image_filenames)) + " ")
    written_file.write(str(r) + " ")
    written_file.write(str(c) + "\n")

    c = 1
    for filename in image_filenames:
        print(c)
        c += 1
        i = Image.open(filename)
        for row in range(r):
            for col in range(c):
                pixel = i.getpixel((col, row))

                written_file.write(str(pixel[0]) + " ")
                written_file.write(str(pixel[1]) + " ")
                written_file.write(str(pixel[2]) + " ")

        written_file.write("\n")




if __name__ == "__main__":
    main()