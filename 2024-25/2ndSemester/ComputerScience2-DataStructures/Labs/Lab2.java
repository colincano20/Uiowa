//DO NOT REMOVE PACKAGE LINE
//Without this line authograder will not run correctly
//You can comment it while you work on the problem
//When everything works - uncomment and submit!
package main.java.com.gradescope.lab2;
import java.util.Arrays;

import static java.lang.Math.*;
/* Please make sure to use good practices of coding
   indent, write comment, use meaningful variable names */
public class Lab2 {
    public static void main(String[] args)
    {

    }

    /* The count method takes an array of integers a
       and a target value t, and returns the number of times t
       occurs in a */

    public static int count(int[] a, int t)
    {
        var count = 0;
        for (int i = 0; i < a.length; i++)
        {
            if (a[i] == t)
            {
                count++;
            }
        }
        return count;
    }

    /* The duplicates method takes an array of Strings s.
       The method returns true if there are duplicate values
       in the array s, and false otherwise.
       Treat all string values as case sensitive. */

    public static boolean duplicates(String[] s)
    {
        for (int i = 0; i < s.length; i++)
        {
            for (int j = 0; j < s.length; j++)
            {
                // The i != j check is to prevent a string from being
                // labeled its own duplicate.
                if (i != j && s[i].equals(s[j]))
                {
                    return true;
                }
            }
        }
        return false;
    }

    /* The stretch method takes an integer array a.
       and returns a new array that has twice as many elements
       as the original a. Each element n of the original array
       corresponds to two elements in the new array. If n is at
       position i in a, the two new elements are at position
       2*i and 2*i + 1 in the new array.
       Moreover, if n is even, the two new elements are each half
       of n. If n is odd, the first element is equal to the second
       plus 1, and their sum equals n. */


    public static int[] stretch(int[] a)
    {
        int[] result = new int[a.length * 2];
        for (int i = 0; i < a.length; i++)
        {
            if (a[i] % 2 == 0)
            {
                result[i*2] = a[i] / 2;
                result[i*2 + 1] = a[i] / 2;
            }
            else
            {
                // Since we want the first number to be the larger one,
                // we add one to the first number before halving it,
                // and subtract one from the second before halving it.
                // For any x, (x + 1) + (x - 1) = 2x.
                result[i*2] = (a[i] + 1) / 2;
                result[i*2 + 1] = (a[i] - 1) / 2;
            }
        }
        return result;
    }
}
