
// DO NOT REMOVE THE PACKAGE LINE!!
// Without this line Autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
//package com.gradescope.HW1;
import java.util.Arrays;
import java.util.Scanner;

//import static java.lang.Math.*;

/* Make sure to use good coding practices such as indenting code, 
   writing comments, use meaningful variable names, and so on 
*/
public class HW1 {
    public static void main(String[] args) {
        // test you code here
        // main will not be graded but it must compile with no errors.

        System.out.println(mismatch("ATCGAT", "TAGCTA")); // Output: 0
        System.out.println(mismatch("ATCGAT", "TAGCAA")); // Output: 1
        System.out.println(mismatch("ATCGAT", "TATCTT")); // Output: 2
        System.out.println(mismatch("ATCG", "TATCTT")); // Output: 3

        System.out.println(Arrays.toString(removeZeros(new int[]{1, -2, 3})));
        System.out.println(Arrays.toString(removeZeros(new int[]{1, 0, 0})));
        System.out.println(Arrays.toString(removeZeros(new int[]{1, 0, -2, 0, 3})));
        System.out.println(Arrays.toString(removeZeros(new int[]{0,0})));

        System.out.println(Arrays.toString(vowelCount("homework")));

        showTwos(7);
        showTwos(18);
        showTwos(68);
        showTwos(120);

        Scanner sc = new Scanner("6 fun. 3 hello 10 <> 2 25 4 wow!");
        printStrings(sc);
    }


public static int mismatch(String a, String b) {
    int count = 0;
    int minLength = Math.min(a.length(), b.length()); // Get the shorter length
    for (int i = 0; i < minLength; i++) {
        if ((a.charAt(i) == 'A' && b.charAt(i) != 'T') ||
            (a.charAt(i) == 'C' && b.charAt(i) != 'G') ||
            (a.charAt(i) == 'G' && b.charAt(i) != 'C')||
            (a.charAt(i) == 'T' && b.charAt(i) != 'A')){ //checks for any mismatches
            count++; //adds to the count if there is a mismatch
        }
    }
    count += (Math.abs(a.length() - b.length())); //if they are different lengths, add the difference to the count
    return count;
}


public static int[] removeZeros(int[] a){
    int count = 0;
    for (int i = 0; i < a.length; i++){
        if ( a[i] == 0){
            count++; //find amount of zeroes in original array
        }
    }
    int[] result = new int[(a.length - count)]; // initialize new array with correct size

    int j = 0; //index for new array
    for (int i = 0; i < a.length; i++){
        if (a[i] != 0){  //Only copy non-zero values
            result[j] = a[i];
            j++; // Move to the next position in the result array

        }

    }
    return result;
}



    public static int[] vowelCount(String input) {
        int[] counts = new int[5]; // Array for [a, e, i, o, u]

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            //if the character is a vowel, add it to the specific index
            if (c == 'a'){
                counts[0]++;
            }
            else if (c == 'e') {
                counts[1]++;
            }
            else if (c == 'i'){
                counts[2]++;
            }
            else if (c == 'o') {
                counts[3]++;
            }
            else if (c == 'u') {
                counts[4]++;
            }
        }
        return counts;
    }


    public static void printStrings(Scanner sc) {
        while (sc.hasNextInt()) {  // While there's an integer available it keeps reading
            int count = sc.nextInt();  // Reads the number of times to repeat
            String word = sc.next();   // Reads the string to be repeated
            for (int i = 0; i < count; i++) {  // Repeat the string 'count' times
                System.out.print(word);
            }
            System.out.println();  // Move to the next line
        }
    }



    public static void showTwos(int n) {
        int initial = n; // store the initial n value
        int count = 0; // count how many loops
        //
        while (n%2 == 0){ //check if the number is even
            n = n/2; // divide the number by 2
            count++;
        }
        System.out.println(initial + " = " + "2 * ".repeat(count) + n);

}

}





























