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

// Problem 1
// The Iterator EveryOther takes a start, end, and input array
// as parameters to its constructor. The sequence it returns
// consists of every other element of input, from start index
// (included) to end index. See EveryOtherTest for examples.

// Your job is to fix any errors in the implementation below of EveryOther. 
// You will likely need to edit the code in more than one place.
public class EveryOther<E> implements Iterator<E> {
        private int current;
        private int end;
        private E[] arr; 

        public EveryOther(int start, int end, E[] arr){
                this.current = start;
                this.end = end;
                this.arr = arr;
        }

        @Override
        public boolean hasNext() {
                return this.current <= end;
        }

        @Override
        public E next() {
                // we recommend putting this first line in ALL of your
                // Iterator.next methods. It ensures that if someone
                // calls next() when hasNext() is false
                // that you raise the appropriate exception
                if (!hasNext()) throw new NoSuchElementException();

                E temp = arr[current];
                current += 2;
                return temp;
        }
}
