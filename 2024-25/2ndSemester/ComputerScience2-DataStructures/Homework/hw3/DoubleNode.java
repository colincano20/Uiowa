// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and su
package com.gradescope.hw3;

/* Header
   Hw 3
   Authors: 
*/

// Due to autograder and junit limitations this class is defined as a separate public class
// However, the best practice is to make it private class inside the DoublyLinkedList class
public class DoubleNode<E> {
    // these fields should be private. They are made public only for testing purposes.
    public DoubleNode<E> prev;
    public DoubleNode<E> next;
    public E elem;

    /**
     * Creates a node with the given element and no previous or next node.
     *
     * @param e  the element to be stored
     */
    public DoubleNode(E e){
        this.elem = e;
        this.prev = null;
        this.next = null;


    }

    /**
     * Creates a node with the given element and previous and next nodes.
     *
     * @param e  the element to be stored
     * @param p  reference to a node that should precede the new node
     * @param n  reference to a node that should follow the new node
     */
    public DoubleNode(DoubleNode<E> p, E e, DoubleNode<E> n){
        this.prev = p;
        this.next = n;
        this.elem = e;
 
    }
}