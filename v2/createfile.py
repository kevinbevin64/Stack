from PIL import Image

def main():
    # open stacked file 
    # read in data
    stacked_file = open("stack.out", "r")
    vals = stacked_file.readlines()
    for i in range(len(vals)):
        vals[i] = vals[i].split();

    x_size = int(vals[0][0])
    y_size = int(vals[0][1])

    # create final image
    master = Image.new(mode="RGB", size=(x_size, y_size))

    for r in range(1, len(vals)):
        for c in range(int(len(vals[r]) / 3)):
            r_pixel = int(vals[r][c * 3])
            g_pixel = int(vals[r][c * 3 + 1])
            b_pixel = int(vals[r][c * 3 + 2])
            master.putpixel((c, r - 1), (r_pixel, g_pixel, b_pixel))

    master.save("master.jpg")



if __name__ == "__main__":
    main()