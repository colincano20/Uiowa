// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.hw3;

public interface PlayList<E> extends List<E> {
    /**
     * Returns (but does not remove) the current element.
     *
     * @return the current element
     * @throws EmptyListException if the list is empty
     */
    E getCurrent() throws EmptyListException;

    /**
     * Chooses the current element to be the one at the given index
     *
     * @param  i the index of the element to designate as current
     * @throws IndexOutOfBoundsException if the index is negative or greater than size()-1
     */
    void chooseCurrent(int i) throws IndexOutOfBoundsException;

    /**
     * Chooses the successor of the current element as the next current element,
     * if such element exits. Otherwise, it does nothing.
     *
     * @throws EmptyListException if the list is empty
     */
    void forward() throws EmptyListException;

    /**
     * Chooses the predecessor of the current element as the next current element,
     * if such element exits. Otherwise, it does nothing.
     *
     * @throws EmptyListException if the list is empty
     */
    void backward() throws EmptyListException;

    /**
     * Chooses the first element of the list as the next current element.
     *
     * @throws EmptyListException if the list is empty
     */
    void restart() throws EmptyListException;
}
