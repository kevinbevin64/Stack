#include "pixel.h"

Pixel::Pixel() {
    r = 0;
    g = 0;
    b = 0;
}

Pixel::Pixel(unsigned int m_r, unsigned int m_g, unsigned int m_b) {
    r = m_r;
    g = m_g;
    b = m_b;
}

Pixel::~Pixel() {}

void Pixel::add(Pixel p) {
    r += p.r;
    g += p.g;
    b += p.b;
}

Pixel Pixel::average(unsigned int count) {
    Pixel p;
    p.r = r / count;
    p.g = g / count;
    p.b = b / count;
    return p;
}
