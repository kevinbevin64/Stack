#include <iostream>
#include "pixel.h"
#include "image.h"

using namespace std;

int main() {
    freopen("stack.in", "r", stdin);
    freopen("stack.out", "w", stdout);

    unsigned short n, x, y;
    cin >> n >> x >> y;

    clog << "Number of pictures: " << n << endl;
    clog << "Image dimensions: " << x << " " << y << endl;

    // initialize the master image
    Image master = Image(x, y);
    master.p_grid = new Pixel*[y];
    for (int i = 0; i < y; i++) {
        master.p_grid[i] = new Pixel[x];
    }

    // ingest the pixel values from input
    // add them to the master image
    clog << "Ingesting the images...";
    for (int i = 0; i < n; i++) {
        clog << "\rIngesting the images... (" << i + 1 << "/" << n << ")\t";
        for (int r = 0; r < y; r++) {
            for (int c = 0; c < x; c++) {
                // clog << i << " " << r << " " << c << endl;
                unsigned int r_pixel, g_pixel, b_pixel;
                cin >> r_pixel >> g_pixel >> b_pixel;
                Pixel p(r_pixel, g_pixel, b_pixel);
                master.p_grid[r][c].add(p);
            }
        }
    }
    clog << "--> Done!" << endl;
    master.count = n;

    // stack the image
    clog << "Stacking the images..." << endl;
    master.stack();

    // write the pixel values to stack.out
    cout << x << " " << y << "\n";
    for (int r = 0; r < y; r++) {
        for (int c = 0; c < x; c++) {
            cout << master.p_grid[r][c].r << " ";
            cout << master.p_grid[r][c].g << " ";
            cout << master.p_grid[r][c].b << " ";
        }
        cout << "\n";
    }
    clog << "Done!" << endl;

    return 0;
}
