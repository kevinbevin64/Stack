#ifndef PIXEL_H
#define PIXEL_H

class Pixel {
public:
    unsigned int r;
    unsigned int g;
    unsigned int b;

    Pixel();
    Pixel(unsigned int m_r, unsigned int m_g, unsigned int m_b);
    ~Pixel();
    void add(Pixel p);
    Pixel average(unsigned int count);
};

#endif