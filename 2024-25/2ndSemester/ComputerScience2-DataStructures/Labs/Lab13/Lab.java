// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.lab;

import net.datastructures.SinglyLinkedList;
import net.datastructures.BinaryTree;
import net.datastructures.Position;

public class Lab {
    // Problem 1
    // Return the sum of only the leaves of the tree
    // Requirement: use recursion
    // HINT: use a helper function.
    public static int sumOfLeaves(BinaryTree<Integer> tree) {
        if (tree.isEmpty()) {
            return 0;
        }
        return sumOfLeavesHelper(tree, tree.root());

    }

    private static int sumOfLeavesHelper(BinaryTree<Integer> tree, Position<Integer> p) {
        int sum = 0;
        if (tree.isExternal(p)) {
            return p.getElement();
        }
        if (tree.left(p) != null) {
            sum += sumOfLeavesHelper(tree, tree.left(p));
        }
        if (tree.right(p) != null) {
            sum += sumOfLeavesHelper(tree, tree.right(p));
        }
        return sum;
    }


    // Problem 2
    // Return the Position which has the largest element among all Positions in the tree
    // Assume that the tree is non-empty. Do not assume that the tree is ordered
    // Requirement: use recursion
    // HINT: use a helper function.
    public static Position<Integer> maxPosition(BinaryTree<Integer> tree) {
        return maxHelper(tree, tree.root());
    }

    private static Position<Integer> maxHelper(BinaryTree<Integer> tree, Position<Integer> p) {
        Position<Integer> max = p;
        if (tree.left(p) != null) {
            Position<Integer> leftMax = maxHelper(tree, tree.left(p));
            if (leftMax.getElement() > max.getElement()) {
                max = leftMax;
            }
        }
        if (tree.right(p) != null) {
            Position<Integer> rightMax = maxHelper(tree, tree.right(p));
            if (rightMax.getElement() > max.getElement()) {
                max = rightMax;
            }
        }
        return max;
    }

    // Problem 3
    // Return a linked list that contains all the values stores the tree leaves, starting
    // with the value in the rightmost leaf and ending with the value in the leftmost leaf
    // Requirement: use recursion
    // HINT: use a helper function that also takes an accumulator list
    public static SinglyLinkedList<Integer> leafList(BinaryTree<Integer> tree) {
        return leafHelper(tree, tree.root(),new SinglyLinkedList<Integer>() );
    }

    private static SinglyLinkedList<Integer> leafHelper(BinaryTree<Integer> tree, Position<Integer> p, SinglyLinkedList<Integer> list) {
        if (tree.isExternal(p)) {
            list.addFirst(p.getElement());
        } else {
            if (tree.left(p) != null) {
                leafHelper(tree, tree.left(p), list);
            }
            if (tree.right(p) != null) {
                leafHelper(tree, tree.right(p), list);
            }

        }
    return list;
    }
}
