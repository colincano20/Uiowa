package com.gradescope.lab;

import net.datastructures.Map;
import net.datastructures.UnsortedTableMap;

public class BigramCounter {
    private final Map<Bigram, Integer> counts;

    public BigramCounter() {
        counts = new UnsortedTableMap<>();
    }

    public void observePair(String word1, String word2) {
        Bigram pair = new Bigram(word1, word2);
        Integer currentCount = counts.get(pair);
        if (currentCount == null) {
            counts.put(pair, 1);
        } else {
            counts.put(pair, currentCount + 1);
        }
    }

    public int getCount(String word1, String word2) {
        Bigram pair = new Bigram(word1, word2);
        Integer count = counts.get(pair);
        if (count == null) {
            return 0;
        } else {
            return count;
        }
    }
}
