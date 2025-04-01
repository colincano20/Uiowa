//DO NOT REMOVE PACKAGE LINE
//Without this line authograder will not run correctly
//You can comment it while you work on the problem
//When everything works - uncomment and submit!
package com.gradescope.lab9;

/*Header
/Lab 9
/Names:
*/
import java.util.Iterator;
import java.util.NoSuchElementException;

// Problem 2
// The constructor of Iterator EveryOther2 takes as input any
// iterator over elements of type E. The sequence it returns
// consists of every other element of iter, starting with 
// the first element of iter. See EveryOther2Test for examples.

public class EveryOther2<E> implements Iterator<E> {
        // you'll need to add instance variables
        Iterator<E> iter;

        public EveryOther2(Iterator<E> iter){
                this.iter = iter;
        }

        @Override
        public boolean hasNext() {
                return iter.hasNext();
        }

        @Override
        public E next() {
                if (!hasNext()) throw new NoSuchElementException();

                E result = iter.next();
                if (hasNext())
                {
                        iter.next();
                }
                return result;
        }
}
