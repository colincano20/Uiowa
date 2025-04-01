//DO NOT REMOVE PACKAGE LINE
//Without this line authograder will not run correctly
//You can comment it while you work on the problem
//When everything works - uncomment and submit!
package com.gradescope.lab9;

/*Header
/Lab 9
/Names:
*/
import java.util.Iterator;
import java.util.NoSuchElementException;

// Problem 3 
// The Iterator EvenIterator, takes an array of Integers as
// the parameter to the constructor. The sequence it returns
// is only the even values in the input. See EvenIteratorTest
// for examples.

// Complete the class
// TIP: check if x is even with: x % 2 == 0
// TIP: keep in mind the FOUR requirements of Iterators! 
// Summarized here
/*
1. hasNext() should keep returning the same value until next() is called again
2. hasNext() should never return true after it has returned false
3. If the last call to hasNext() was true, then the following call to next() should succeed!
4. If hasNext() returned (or would return false), then next() should fail, indicated by a NoSuchElementException
 */
public class EvenIterator implements Iterator<Integer> {
    /*
    - Approach A: ignore approach B and C; you are on your own :)
    - Approach B: pre-compute all the results into a List, during the constructor
           - Approach B option 1: suggested instance variable is an Iterator, from calling iterator() on the results List
           - Approach B option 2: suggested instance variables are a List and current index
    - Approach C: identify an invariant; as long as your Iterator has more elements to return, your
                    invariant should still be true, except for temporarily becoming false during the
                    middle of the constructor code or the next code.
           - suggested instance variables are an array and current index
     */
    private Integer[] arr;
    private int current;

    public EvenIterator(Integer[] arr) {
        this.arr = arr;
        this.current = 0;
        while (current < arr.length && arr[current] % 2 != 0)
        {
            current++;
        }
    }

    @Override
    public boolean hasNext() {
        return current < arr.length;
    }

    @Override
    public Integer next()
    {
        if (!hasNext()) throw new NoSuchElementException();

        Integer result = arr[current];
        current++;
        while (current < arr.length && arr[current] % 2 != 0)
        {
            current++;
        }
        return result;
    }
}
