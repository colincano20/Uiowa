// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.lab;

import net.datastructures.UnsortedTableMap;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class MapBag<T> implements Bag<T> {
    private final UnsortedTableMap<T,Integer> b = new UnsortedTableMap<>();

    /* Return the number of occurrences of e in the set. */
    public int multiplicity(T e) {
        if (!contains(e)) {
            return 0;
        }
        return b.get(e);  // replace with your implementation
    }

    /* Increase the multiplicity of e in the set by 1. */
    public void add(T e) {
        if (!contains(e)) {
            b.put(e, 1);
            return;
        }
        b.put(e, b.get(e) + 1);
    }

    /* Return true if e is in the set (with any positive multiplicity), and false otherwise */
    public boolean contains(T e) {
        return (b.get(e) != null) && (b.get(e) > 0);  // replace with your implementation
    }

    /* Return true if the bag is empty, and false otherwise */
    public boolean isEmpty() {
        return b.isEmpty();  // replace with your implementation
    }

    /* Decrease the multiplicity of e in the set by 1 if e was already in there.
       Otherwise, do nothing.
       Return true if e was in the set and false otherwise */
    public boolean removeOne(T e) {
        if (!contains(e)) {
            return false;
        }
        if (b.get(e) == 1) {
            remove(e); // replace with your implementation
        }
        else {
            b.put(e, b.get(e) - 1);
        }
        return true;
    }

    /* remove e completely from the set.
       Return true if e was in the set and false otherwise */
    public void remove(T e) {
         if (!contains(e)) {
             return;
         }
         b.remove(e);
    }

    /* return the number of elements in this set, irrespective of their multiplicities */
    public  int size() {
        return b.size();  // replace with your implementation
    }

    /* return an iterator over the elements in the set.
       The iterator does not need to return elements
       in any particular order */
    public Iterator<T> iterator() {
        var entries = b.entrySet().iterator();
        var keys = new ArrayList<T>();
        while (entries.hasNext()) {
            keys.add(entries.next().getKey());
        }
        return keys.iterator();
    }
}
