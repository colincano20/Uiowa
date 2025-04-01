// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.hw3;

/* Header
   Hw 3
   Authors: Colin Cano
*/

public class ArrayList<E> implements PlayList<E> {
    // instance variables
    public static final int CAPACITY = 16;     // default array capacity

    /** Generic array used for storage of list elements. */
    private E[] elems;
    /** Index of current element in the list.
     *  It should be a private field.
     *  We make it public for the assignment, for testing purposes
     */
    public int current = -1;
    /** Current number of elements in the list. */
    private int size = 0;

    // constructors
    /** Creates an array list with default initial capacity. */
    public ArrayList() {
        this(CAPACITY);
    }

    /** Creates an array list with given initial capacity. */
    @SuppressWarnings({"unchecked"})
    public ArrayList(int capacity) {
        elems = (E[]) new Object[capacity];     // safe cast; compiler may give warning
    }

    // public methods
    /**
     * Returns the number of elements in the list.
     * @return number of elements in the list
     */

    @Override
    public int size() { return size; }

    /**
     * Tests whether the array list is empty.
     * @return true if the array list is empty, false otherwise
     */
    @Override
    public boolean isEmpty() { return size == 0; }

    /**
     * Returns (but does not remove) the element at index i.
     * @param  i   the index of the element to return
     * @return the element at the specified index
     * @throws IndexOutOfBoundsException if the index is negative or greater than size()-1
     */
    @Override
    public E get(int i) throws IndexOutOfBoundsException {
        checkIndex(i, size);
        return elems[i];
    }

    /**
     * Replaces the element at the specified index, and returns the element previously stored.
     * @param  i   the index of the element to replace
     * @param  e   the new element to be stored
     * @return the previously stored element
     * @throws IndexOutOfBoundsException if the index is negative or greater than size()-1
     */
    @Override
    public E set(int i, E e) throws IndexOutOfBoundsException {
        checkIndex(i, size);
        E temp = elems[i];
        elems[i] = e;
        return temp;
    }

    @Override
    public void append(E e) {
        insert(size, e);
        if (size == 1) { //if list is empty before appending element, current set to 0.
            current = 0;
        }
    }

    /**
     * Inserts the given element at the specified index of the list, shifting all
     * subsequent elements in the list one position further to make room.
     * @param  i   the index at which the new element should be stored
     * @param  e   the new element to be stored
     * @throws IndexOutOfBoundsException if the index is negative or greater than size()
     */
    @Override
    public void insert(int i, E e) throws IndexOutOfBoundsException {
        checkIndex(i, size + 1);
        if (size == elems.length) {
            resize(2 * elems.length);
        }
        for (int k = size - 1; k >= i; k--) {
            elems[k + 1] = elems[k];
        }
        elems[i] = e;
        size++;
        if (current >= i) { //if current is at or after o, it moves 1.
            current++;
        }
    }
    /**
     * Removes and returns the element at the given index, shifting all subsequent
     * elements in the list one position closer to the front.
     * @param  i the index of the element to be removed
     * @return the element that had be stored at the given index
     * @throws IndexOutOfBoundsException if the index is negative or greater than size()
     */
    @Override
    public E remove(int i) throws IndexOutOfBoundsException {
        checkIndex(i, size);
        E temp = elems[i];
        for (int k = i; k < size - 1; k++) {
            elems[k] = elems[k + 1];
        }
        size--;
        if (size == 0) {
            current = -1; //checks for empty list and then sets current to -1
        } else if (current == i) {
            current = (size > 0) ? 0 : -1; // if removed element was current, current is set to 0
        } else if (current > i) {
            current--; //if element before current is removed, move left 1.
        }
        return temp;
    }

    //===================
    // Auxiliary methods
    //===================
    /** Checks whether the given index is in the range [0, n-1]. */
    protected void checkIndex(int i, int n) throws IndexOutOfBoundsException {
        if (i < 0 || i >= n) {
            throw new IndexOutOfBoundsException("Illegal index: " + i);
        }
    }
    /** Resizes internal array to have given capacity >= size. */
    @SuppressWarnings("unchecked")
    protected void resize(int capacity) {
        E[] temp = (E[]) new Object[capacity]; // safe cast; compiler may give warning
        for (int k = 0; k < size; k++) {
            temp[k] = elems[k];
        }
        elems = temp; // start using the new array
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("[");
        for (int j = 0; j < size; j++) {
            if (j > 0) sb.append(", ");
            sb.append(elems[j]);
        }
        sb.append("]");
        return sb.toString();
    }

    //===================
    // PlayList methods
    //===================
    @Override
    public E getCurrent() throws EmptyListException {
        if (size == 0) {
            throw new EmptyListException("List is empty");
        }
        return elems[current];
    }

    /**
     * Chooses the current element to be the one at the given index
     *
     * @param  i the index of the element to designate as current
     * @throws IndexOutOfBoundsException if the index is negative or greater than size()-1
     */
    @Override
    public void chooseCurrent(int i) throws IndexOutOfBoundsException {
        checkIndex(i, size);
        current = i;
    }
    /**
     * Chooses the successor of the current element as the next current element,
     * if such element exits. Otherwise, it does nothing.
     *
     * @throws EmptyListException if the list is empty
     */
    @Override
    public void forward() throws EmptyListException {
        if (size == 0) {
            throw new EmptyListException("List is empty");
        }
        if (current < size - 1) {
            current++;
        }
    }

    /**
     * Chooses the predecessor of the current element as the next current element,
     * if such element exits. Otherwise, it does nothing.
     *
     * @throws EmptyListException if the list is empty
     */
    @Override
    public void backward() throws EmptyListException {
        if (size == 0) {
            throw new EmptyListException("List is empty");
        }
        if (current > 0) {
            current--;
        }
    }
    /**
     * Chooses the first element of the list as the next current element.
     *
     * @throws EmptyListException if the list is empty
     */
    @Override
    public void restart() throws EmptyListException {
        if (size == 0) {
            throw new EmptyListException("List is empty");
        }
        current = 0;
    }
}
