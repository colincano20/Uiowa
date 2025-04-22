// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.lab;

/* An unordered collection that can contain each element multiple times  */

public interface Bag<T> extends Iterable<T> {

    /* Return the number of occurrences of e in the set. */
    int multiplicity(T e);

    /* Increase the multiplicity of e in the set by 1. */
    void add(T e);

    /* Return true if e is in the set (with any positive multiplicity), and false otherwise */
    boolean contains(T e);

    /* Return true if the bag is empty, and false otherwise */
    boolean isEmpty();

    /* Decrease the multiplicity of e in the set by 1 if e was already in there.
       Otherwise, do nothing.
       Return true if e was in the set and false otherwise */
    boolean removeOne(T e);

    /* remove e completely from the set. Do nothing if e was not in the set */
    void remove(T e);

    /* return the number of elements in this set, irrespective of their multiplicities */
    int size();
}
