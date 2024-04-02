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

void Pixel::average(unsigned int count) {
    r = r / count;
    g = g / count;
    b = b / count;
}
