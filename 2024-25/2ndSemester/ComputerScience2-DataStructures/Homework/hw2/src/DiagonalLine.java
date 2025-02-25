package com.gradescope.hw2;
import bridges.base.Color;
import bridges.base.ColorGrid;

public class DiagonalLine extends Mark {
    // The line is characterized by its start and end points.
    // xs and ys store the start point coordinates
    private final int xs;
    private final int ys;
    // xe and ye store the end point coordinates
    private final int xe;
    private final int ye;

    public DiagonalLine(int x0, int y0, int x1, int y1, Color color) {
        this.xs = x0;
        this.xe = x1;
        this.ys = y0;
        this.ye = y1;
        this.color = color;

    }

    @Override
    public void draw(ColorGrid cg) {
        int dx = Math.abs(xe - xs);
        int dy = Math.abs(ye - ys);
        int sx = (xs < xe) ? 1 : -1;
        int sy = (ys < ye) ? 1 : -1;
        int err = dx - dy;

        int x = xs, y = ys;

        while (true) {
            cg.set(y, x, this.color); // Set pixel
            if (x == xe && y == ye) break;
            int e2 = 2 * err;
            if (e2 > -dy) {
                err -= dy;
                x += sx;
            }
            if (e2 < dx) {
                err += dx;
                y += sy;
            }
        }
    }
}
