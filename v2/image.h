#ifndef IMAGE_H
#define IMAGE_H

#include "pixel.h"

class Image {
public:
    unsigned short x;
    unsigned short y;
    Pixel** p_grid;
    unsigned int count;

    Image();
    Image(unsigned short m_x, unsigned short m_y);
    Image(unsigned short m_x, unsigned short m_y, Pixel **m_p_grid);
    ~Image();
    void add(Image i);
    void stack();
};

#endif