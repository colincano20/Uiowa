// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.lab5;

/* Header
   Lab 5
   Authors:
*/

import java.util.List;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Random;

public class ListApp {
    public static void main(String[] args) {
        Random r = new Random(2230);

        List<Integer> l1 = new LinkedList<>();
        List<String> l2 = new ArrayList<>();    
        for (int i=0; i<6; i++) {
            Integer x = r.nextInt(10);
            l1.add(x);
        }
        for (int i=0; i<10; i++) {
            String s = randomString(r);
            l2.add(s);
        }

        System.out.println("BEFORE");
        System.out.println("l1: " + l1);
        System.out.println("l2: " + l2);

        swapFL(l1);
        swapFL(l2);
        
        System.out.println("\nAFTER");
        System.out.println("l1: " + l1);
        System.out.println("l2: " + l2);
    }

    /**
    Swaps the first and last elements of the list

    By taking List as the parameter type instead of a 
    specific kind of List (e.g., LinkedList or ArrayList)
    we only need to write ONE method! You don't need
    a separate method for LinkedList and ArrayList.

    And by taking a List with generic type E, you only
    need to write ONE method! You don't need a separate method
    for List<Integer> and List<String>.
    **/
    public static <E> void swapFL(List<E> ls) {
        if (ls.size() == 0) {
            return;
        }
        E first = ls.get(0);
        E last = ls.get(ls.size() - 1);

        ls.set(0, last);
        ls.set(ls.size() - 1, first);
    }

    public static String randomString(Random r) {
        final String chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 4; i++) {
            sb.append(chars.charAt(r.nextInt(chars.length())));
        }
        return sb.toString();
    }
}
