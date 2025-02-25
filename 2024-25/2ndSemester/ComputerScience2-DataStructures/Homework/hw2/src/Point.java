package com.gradescope.hw2;
import bridges.base.Color;
import bridges.base.ColorGrid;

public class Point extends Mark {
    private final int x;
    private final int y;

    public Point(int x, int y, Color c) {
        this.x =x;
        this.y =y;
        this.color = c;

    }
    @Override
    public void draw(ColorGrid cg) {
        cg.set(this.y, this.x, this.color);



    }
}
