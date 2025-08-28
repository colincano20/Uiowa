// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.hw;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class RisingIterator implements Iterator<Integer> {
    private Iterator<Integer> input;
    private Integer last;
    private Integer next;
    private boolean hasNext;

    public RisingIterator(Iterator<Integer> input) {
        this.input = input;
        last = null;

        // Initialize next with the first value that is valid
        while (input.hasNext()) {
            Integer current = input.next();
            next = current;
            hasNext = true;
            last = current;
            break;
        }

        if (!hasNext) {
            hasNext = false;
        }
    }




    @Override
    public boolean hasNext() {
        // replace this body with your implementation
        return hasNext;
    }

    @Override
    public Integer next() {
        // replace this body with your implementation
        if (!hasNext) throw new NoSuchElementException();
        Integer result = next;

        // Find the next strictly increasing value
        hasNext = false;
        while (input.hasNext()){
            Integer current = input.next();
            if (current > last) {
                next = current;
                hasNext = true;
                last = current;
                break;

            }
        }
        return result;
    }
}
