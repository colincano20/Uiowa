//DO NOT REMOVE PACKAGE LINE
//Without this line authograder will not run correctly
//You can comment it while you work on the problem
//When everything works - uncomment and submit!
package com.gradescope.lab1pr1;

public class Problem1 {
    /*Find all the problems (bugs)
    / fix the errors (explain in comments what you did to fix it!)
    / When the program is fixed. Run it. 
    /Correct run will print:
    /Hello Class!
    / 12
    /This is 17
    */

    public static void main(String[] args) {
        String x = "Hello Class!"; //changed the type to String since wasn't floating point
        System.out.println(x); // added semicolon
        int z = 7 + 5; //changed variable to z
        System.out.println(z); //changed variable to z to fix logic
        int y = z + 4; //added int in front of variable name
        y += 1;
        System.out.println("This is " + y); // Added the + in front of y
    }
}