// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.lab4;

/* Header
   Lab 4
   Authors:
*/

/*
 * Copyright 2014, Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser
 *
 * Developed for use with the book:
 *
 *    Data Structures and Algorithms in Java, Sixth Edition
 *    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
 *    John Wiley & Sons, 2014
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
//package net.datastructures;

/**
 * A basic singly linked list implementation.
 *
 * @author Michael T. Goodrich
 * @author Roberto Tamassia
 * @author Michael H. Goldwasser
 */

/* CS2230
This version of IntSinglyLinkedList replaces the generic type in SinglyLinkedList
with Integer. It may be easier to read if you haven't seen
generic types (reading assignment for Week 4)
*/

public class IntSinglyLinkedList {
    //---------------- nested Node class ----------------
    /**
     * Node of a singly linked list, which stores a reference to its
     * element and to the subsequent node in the list (or null if this
     * is the last node).
     */
    private static class Node {

        /** The element stored at this node */
        private Integer element;            // reference to the element stored at this node

        /** A reference to the subsequent node in the list */
        private Node next;         // reference to the subsequent node in the list

        /**
         * Creates a node with the given element and next node.
         *
         * @param e  the element to be stored
         * @param n  reference to a node that should follow the new node
         */
        public Node(Integer e, Node n) {
            element = e;
            next = n;
        }

        // Accessor methods
        /**
         * Returns the element stored at the node.
         * @return the element stored at the node
         */
        public Integer getElement() { return element; }

        /**
         * Returns the node that follows this one (or null if no such node).
         * @return the following node
         */
        public Node getNext() { return next; }

        // Modifier methods
        /**
         * Sets the node's next reference to point to Node n.
         * @param n    the node that should follow this one
         */
        public void setNext(Node n) { next = n; }
    } //----------- end of nested Node class -----------

    // instance variables of the IntSinglyLinkedList
    /** The head node of the list */
    private Node head = null;               // head node of the list (or null if empty)

    /** The last node of the list */
    private Node tail = null;               // last node of the list (or null if empty)

    /** Number of nodes in the list */
    private int size = 0;                      // number of nodes in the list

    /** Constructs an initially empty list. */
    public IntSinglyLinkedList() { }              // constructs an initially empty list

    // access methods
    /**
     * Returns the number of elements in the linked list.
     * @return number of elements in the linked list
     */
    public int size() { return size; }

    /**
     * Tests whether the linked list is empty.
     * @return true if the linked list is empty, false otherwise
     */
    public boolean isEmpty() { return size == 0; }

    /**
     * Returns (but does not remove) the first element of the list
     * @return element at the front of the list (or null if empty)
     */
    public Integer first() {             // returns (but does not remove) the first element
        if (isEmpty()) return null;
        return head.getElement();
    }

    /**
     * Returns (but does not remove) the last element of the list.
     * @return element at the end of the list (or null if empty)
     */
    public Integer last() {              // returns (but does not remove) the last element
        if (isEmpty()) return null;
        return tail.getElement();
    }

    // update methods
    /**
     * Adds an element to the front of the list.
     * @param e  the new element to add
     */
    public void addFirst(Integer e) {                // adds element e to the front of the list
        head = new Node(e, head);              // create and link a new node
        if (size == 0)
            tail = head;                           // special case: new node becomes tail also
        size++;
    }

    /**
     * Adds an element to the end of the list.
     * @param e  the new element to add
     */
    public void addLast(Integer e) {                 // adds element e to the end of the list
        Node newest = new Node(e, null);    // node will eventually be the tail
        if (isEmpty())
            head = newest;                         // special case: previously empty list
        else
            tail.setNext(newest);                  // new node after existing tail
        tail = newest;                           // new node becomes the tail
        size++;
    }

    /**
     * Removes and returns the first element of the list.
     * @return the removed element (or null if empty)
     */
    public Integer removeFirst() {                   // removes and returns the first element
        if (isEmpty()) return null;              // nothing to remove
        Integer answer = head.getElement();
        head = head.getNext();                   // will become null if list had only one node
        size--;
        if (size == 0)
            tail = null;                           // special case as list is now empty
        return answer;
    }

    @SuppressWarnings({"unchecked"})
    public boolean equals(Object o) {
        if (o == null) return false;
        if (getClass() != o.getClass()) return false;
        IntSinglyLinkedList other = (IntSinglyLinkedList) o;   // use nonparameterized type
        if (size != other.size) return false;
        Node walkA = head;                               // traverse the primary list
        Node walkB = other.head;                         // traverse the secondary list
        while (walkA != null) {
            if (!walkA.getElement().equals(walkB.getElement())) return false; //mismatch
            walkA = walkA.getNext();
            walkB = walkB.getNext();
        }
        return true;   // if we reach this, everything matched successfully
    }

    /*
    Moves all elements earlier in the list by 1.
    Except it moves the first element to the end
     */
    public void rotateLeft() {
        if (isEmpty() || head.getNext() == null) return;
        Node first = head; //Stores a copy of the first node as the head
        head = head.getNext(); //moves the head to the next node
        tail.setNext(first); //connects old head to the tail
        tail = first; //updates the tail pointer
    }

    /*
    Add the given integer to be the second element of the list

    Won't be called on an empty list
     */
    public void addSecond(Integer e) {
        head.setNext(new Node(e, head.getNext()));
        size++; //Increases the size of list to fit the new node
        if (size == 2) { //checks to see if list has size of 2
            tail = head.getNext(); //updates the tail
        }
    }

    /**
     * Produces a string representation of the contents of the list.
     * This exists for debugging purposes only.
     */
    public String toString() {
        StringBuilder sb = new StringBuilder("(");
        Node walk = head;
        while (walk != null) {
            sb.append(walk.getElement());
            if (walk != tail)
                sb.append(", ");
            walk = walk.getNext();
        }
        sb.append(")");
        return sb.toString();
    }

    public static void main(String[] args) {
        IntSinglyLinkedList sl = new IntSinglyLinkedList();
        sl.addLast(100);
        sl.addLast(200);
        sl.addLast(300);
        System.out.println(sl.toString());
        sl.addSecond(50);
        System.out.println(sl.toString());
    }
}
