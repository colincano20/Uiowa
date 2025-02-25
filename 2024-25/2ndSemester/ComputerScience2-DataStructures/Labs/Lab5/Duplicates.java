package com.gradescope.lab5;
import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;
public class Duplicates {
    public static void main(String[] args) {
        LinkedList<Integer> test1 = new LinkedList<>();
        LinkedList<Integer> test2 = new LinkedList<>();
        LinkedList<Integer> test3 = new LinkedList<>();
        LinkedList<Integer> test4 = new LinkedList<>();

        test1.add(-1);
        test1.add(1);
        test1.add(2);

        test3.add(4);
        test3.add(22);
        test3.add(100);
        test3.add(99);
        test3.add(22);
        test3.add(5);
        test3.add(7);

        test4.add(4);
        test4.add(22);
        test4.add(100);
        test4.add(4);
        test4.add(99);
        test4.add(1);
        test4.add(5);
        test4.add(7);

        System.out.println(noDuplicates(test1));
        System.out.println(noDuplicates(test2));
        System.out.println(noDuplicates(test3));
        System.out.println(noDuplicates(test4));
    }
    public static boolean noDuplicates(List<Integer> list) {
        List<Integer> elements = new LinkedList<>();
        for (Integer element : list) {
            if (elements.contains(element)) return false;
            else elements.add(element);
        }
        return true;
    }
}
