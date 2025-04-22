package com.gradescope.lab;

import java.util.Objects;

public class Bigram {
    private final String w1;
    private final String w2;

    public Bigram(String w1, String w2) {
        this.w1 = w1;
        this.w2 = w2;
    }

    public String getFirst() {
        return w1;
    }

    public String getSecond() {
        return w2;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Bigram)) return false;
        Bigram other = (Bigram) obj;
        return Objects.equals(w1, other.w1) && Objects.equals(w2, other.w2);
    }

    @Override
    public int hashCode() {
        return Objects.hash(w1, w2);
    }
}
