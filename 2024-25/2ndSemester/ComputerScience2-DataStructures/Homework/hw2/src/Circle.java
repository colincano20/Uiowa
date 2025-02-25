package com.gradescope.hw2;
import bridges.base.Color;
import bridges.base.ColorGrid;

public class Circle extends Mark {
    private final int r;  // radius
    private final int xc; // center x-coordinate
    private final int yc; // center y-coordinate

    public Circle(int radius, int xc, int yc, Color color) {
        this.r = radius;
        this.xc = xc;
        this.yc = yc;
        this.color = color;


    }

    private void octantSymm(int xc, int yc, int x, int y, ColorGrid cg) {
        cg.set(yc + y, xc + x, this.color); // Quadrant 1
        cg.set(yc + y, xc - x, this.color); // Quadrant 2
        cg.set(yc - y, xc + x, this.color); // Quadrant 3
        cg.set(yc - y, xc - x, this.color); // Quadrant 4
        cg.set(yc + x, xc + y, this.color); // Quadrant 5
        cg.set(yc + x, xc - y, this.color); // Quadrant 6
        cg.set(yc - x, xc + y, this.color); // Quadrant 7
        cg.set(yc - x, xc - y, this.color); // Quadrant 8
    }

    @Override
    public void draw(ColorGrid cg) {
        int x = 0;
        int y = r;
        int d = 3 - 2 * r;
        octantSymm(xc, yc, x, y, cg);
        while (y >= x) {
            x++;
            if (d > 0) {
                y--;
                d = d + 4 * (x - y) + 10;
            } else d = d + 4 * x + 6;
            octantSymm(xc, yc, x, y, cg);
        }
    }
}
