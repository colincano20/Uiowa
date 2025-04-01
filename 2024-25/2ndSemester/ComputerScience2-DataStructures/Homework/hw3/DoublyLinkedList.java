// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.hw3;

/* Header
   Hw 3
   Authors: 
*/

public class DoublyLinkedList<E> implements PlayList<E> {

    // instance variables of the DoublyLinkedList
    // head and tail should be private. We are making them public now for testing purposes.
    public DoubleNode<E> head = null;
    public DoubleNode<E> tail = null;
    private int size = 0;                      // number of elements in the list
    /**
     * Index of current element in the list.
     * It should be a private field.
     * We make it public for the assignment, for testing purposes
     */
    public DoubleNode<E> current = null;

    /**
     * Constructs a new empty list.
     */
    public DoublyLinkedList() {


    }

    // public accessor methods

    /**
     * Returns the number of elements in the linked list.
     *
     * @return number of elements in the linked list
     */
    @Override
    public int size() {
        return size;
    }

    /**
     * Tests whether the list is empty.
     *
     * @return true if the linked list is empty, false otherwise
     */
    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Returns (but does not remove) the element at index i.
     *
     * @param i the index of the element to return
     * @return the element at the specified index
     * @throws IndexOutOfBoundsException if the index is negative or greater than size()-1
     */
    @Override
    public E get(int i) throws IndexOutOfBoundsException {
        checkIndex(i, size);
        DoubleNode<E> node  = head;
        for (int j = 0; j < i; j++){
            node = node.next;
        }
        return node.elem;
    }

    /**
     * Replaces the element at the specified index, and returns the element previously stored.
     *
     * @param i the index of the element to replace
     * @param e the new element to be stored
     * @return the previously stored element
     * @throws IndexOutOfBoundsException if the index is negative or greater than size()-1
     */
    @Override
    public E set(int i, E e) throws IndexOutOfBoundsException {
        checkIndex(i, size);
        DoubleNode<E> node = head;
        for (int j = 0; j < i; j++) {
            node = node.next;
        }
        E temp = node.elem;
        node.elem = e; // Actually replace the element
        return temp;
    }


    /**
     * Adds the given element at the end of the list.
     *
     * @param e the new element to be stored
     */
    @Override
    public void append(E e) {
        DoubleNode<E> newNode = new DoubleNode<>(e);
        if (isEmpty()){
            head  = tail = current = newNode; // if empty set everything equal to each other
        } else{
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
        size++;
    }

    /**
     * Inserts the given element at the specified index of the list, shifting all
     * subsequent elements in the list one position further to make room.
     *
     * @param i the index at which the new element should be stored
     * @param e the new element to be stored
     * @throws IndexOutOfBoundsException if the index is negative or greater than size()-1
     */
    // to be double-checked
    //
    @Override
    public void insert(int i, E e) throws IndexOutOfBoundsException {
        checkIndex(i, size + 1);
        DoubleNode<E> newNode = new DoubleNode<>(e);

        if (i == 0) { // Inserting at head
            newNode.next = head;
            if (head != null) {
                head.prev = newNode;
            }
            head = newNode;
            if (size == 0) { // If the list was empty, set tail and current
                tail = newNode;
                current = newNode;
            }
        } else if (i == size) { // Inserting at tail
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        } else { // Inserting in the middle
            DoubleNode<E> node = head;
            for (int j = 0; j < i - 1; j++) {
                node = node.next;
            }
            newNode.next = node.next;
            newNode.prev = node;
            if (node.next != null) {
                node.next.prev = newNode;
            }
            node.next = newNode;
        }

        size++;
    }


    /**
     * Removes and returns the element at the given index, shifting all subsequent
     * elements in the list one position closer to the front.
     *
     * @param i the index of the element to be removed
     * @return the element that had be stored at the given index
     * @throws IndexOutOfBoundsException if the index is negative or greater than size()
     */
    @Override
    public E remove(int i) throws IndexOutOfBoundsException {
        checkIndex(i, size);
        DoubleNode<E> node = head;

        for (int j = 0; j < i; j++) {
            node = node.next;
        }

        if (node == head) {
            head = node.next;
            if (head != null) {
                head.prev = null;
            } else {
                tail = null; // If list becomes empty, set tail to null
            }
        } else if (node == tail) {
            tail = node.prev;
            if (tail != null) {
                tail.next = null;
            }
        } else {
            node.prev.next = node.next;
            node.next.prev = node.prev;
        }

        // Adjust current if needed
        if (node == current) {
            current = (head != null) ? head : null;
        }

        size--;
        return node.elem;
    }



    //===================
    // Auxiliary methods
    //===================

    /** Checks whether the given index is in the range [0, n-1]. */
    protected void checkIndex(int i, int n) throws IndexOutOfBoundsException {
        if (i < 0 || i >= n)
            throw new IndexOutOfBoundsException("Illegal index: " + i);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("[");
        DoubleNode<E> n = head;
        for (int j = 0; j < size; j++) {
            if (j > 0) sb.append(", ");
            sb.append(n.elem.toString());
            n = n.next;
        }
        sb.append("]");
        return sb.toString();
    }

    //===================
    // PlayList methods
    //===================

    /**
     * Returns (but does not remove) the current element.
     *
     * @return the current element
     * @throws EmptyListException if the list is empty
     */
    @Override
    public E getCurrent() throws EmptyListException {
        if (isEmpty()) {
            throw new EmptyListException("List is empty");
        }
        return current.elem;
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
        current = head;
        for (int j = 0; j < i; j++) {
            current = current.next;
        }
    }

    /**
     * Chooses the successor of the current element as the next current element,
     * if such element exits. Otherwise, it does nothing.
     *
     * @throws EmptyListException if the list is empty
     */
    public void forward() throws EmptyListException {
        if (isEmpty()) {
            throw new EmptyListException("List is empty");
        }
        if (current.next != null) {
            current = current.next;
        }
    }

    /**
     * Chooses the predecessor of the current element as the next current element,
     * if such element exits. Otherwise, it does nothing.
     *
     * @throws EmptyListException if the list is empty
     */
    public void backward() throws EmptyListException {
        if (isEmpty()) {
            throw new EmptyListException("List is empty");
        }
        if (current.prev != null){
            current = current.prev;
        }
    }

    /**
     * Chooses the first element of the list as the next current element.
     *
     * @throws EmptyListException if the list is empty
     */
    public void restart() throws EmptyListException {
        if (isEmpty()) {
            throw new EmptyListException("List is empty");
        }
        current = head;
    }
}