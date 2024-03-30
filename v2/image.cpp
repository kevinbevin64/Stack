#include "image.h"

Image::Image() {}

Image::Image(unsigned short m_x, unsigned short m_y) {
    x = m_x;
    y = m_y;

    p_grid = new Pixel*[y];
    for (unsigned short i = 0; i < y; i++) {
        p_grid[i] = new Pixel[x];
    }
    
    count = 1;
}

Image::Image(unsigned short m_x, unsigned short m_y, Pixel** m_p_grid) {
    x = m_x;
    y = m_y;

    p_grid = m_p_grid;
    
    count = 1;
}

Image::~Image() {}

void Image::add(Image i) {
    count += i.count;
    for (int r = 0; r < y; r++) {
        for (int c = 0; c < x; c++) {
            p_grid[r][c].add(i.p_grid[r][c]);
        }
    }
}

void Image::stack() {
    for (int r = 0; r < y; r++) {
        for (int c = 0; c < x; c++) {
            p_grid[r][c].average(count);
        }
    }
    count = 1;
}
