// DO NOT REMOVE THE PACKAGE LINE
// Without this line authograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
//
package com.gradescope.lab3;

/* Lab 3

   Authors: Aharon Zingman, Colin Cano, Tyler Kennedy
*/

import java.util.Scanner;

public class TestRandomWalker {
    public static void main(String[] args){
        //Create a RandomWalker called r
        RandomWalker r = new RandomWalker();

        //ask user to type an integer number of steps
        System.out.println("Type integer numeber to represent number of steps to take");
        // Assume the answer provided is indeed integer,
        //no need to check
        Scanner scanner = new Scanner(System.in);
        int steps = scanner.nextInt();

        //you want to take numberofsteps using the move()
        //Each time object moves print result on the console
        for (int i = 0; i < steps; i++) {
            r.move();
            System.out.println(r);
        }
    }
}
