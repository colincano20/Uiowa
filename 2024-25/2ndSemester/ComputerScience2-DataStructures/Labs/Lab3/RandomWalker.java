
// DO NOT REMOVE THE PACKAGE LINE
// Without this line authograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
//
//package com.gradescope.lab3;

/* Lab 3

   Authors: Aharon Zingman, Colin Cano, Tyler Kennedy
*/


import java.util.Random;

public class RandomWalker {
    //declare your fields below (private integers only)
    private int X;
    private int Y;
    private int Steps;

    //Write a constructor. Doesn't accept any parameters ()
    //and constructors never return things!
    public RandomWalker() {
        X = 0;
        Y = 0;
        Steps = 0;
    }

    //getX
    public int getX() {
        return X;
    }

    //getY
    public int getY() {
        return Y;
    }

    //getSteps
    public int getSteps() {
        return Steps;
    }

    //move - don't change declaration!
    public void move(){
        //Create Random variable and "roll" it
        Random rng = new Random();
        int direction = rng.nextInt(4);

        //depending on the roll: up (0), down (1), left (2), or right(3)
        //make your move
        switch (direction) {
            case 0:
                Y++;
                break;
            case 1:
                Y--;
                break;
            case 2:
                X--;
                break;
            case 3:
                X++;
                break;
        }

        Steps++;
    }

    public String toString() {
        return "(" + X + ", " + Y + "), steps = " + Steps;
    }
}
