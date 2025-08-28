// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.hw;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class EveryNthIterator<E> implements Iterator<E> {

    private int nth;
    private Iterator<E> input;
    private int count;
    private E element;

    public EveryNthIterator(Iterator<E> in, int n) {
        this.input = in;
        this.nth = n;
        this.count = 0;
        this.element = null;
    }

    @Override
    public boolean hasNext() {
        return input.hasNext();
    }

    @Override
    public E next() {
        if (!hasNext()) throw new NoSuchElementException();

        // gets the current element
        element = input.next();

        // iterate to the next element for next call
        while(input.hasNext() && this.count < this.nth-1) {
            input.next();
            count++;
        }

        // resets the counter
        count = 0;

        // returns the correct element
        return element;
    }
}