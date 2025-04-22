// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.lab;

public class Bigram implements Comparable<Bigram>{
    public final String w1;
    public final String w2;

    public Bigram(String w1, String w2) {
        this.w1 = w1;
        this.w2 = w2;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Bigram) {
            Bigram big = (Bigram) obj;
            return (w1.equals(big.w1) && w2.equals(big.w2));
        }
        else
        {
            return false;
        }
    }

    @Override
    public int hashCode() {
        String combined = w1 + w2;
        return combined.hashCode(); // replace with your implementation
    }

    @Override
    public int compareTo(Bigram that) {
        switch (w1.compareTo(that.w1))
        {
            case 0:
                return w2.compareTo(that.w2);
            default: return w1.compareTo(that.w1);
        }
    }
}
