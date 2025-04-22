package com.gradescope.lab;

import net.datastructures.Map;
import net.datastructures.UnsortedTableMap;

import java.util.List;

public class CountDuplicatedNumbers {
    public static int countDuplicatedNumbers(List<Integer> numbers) {
        Map<Integer, Integer> m = new UnsortedTableMap<>();
        int count = 0;

        for (int num : numbers) {
            Integer existing = m.get(num);
            if (existing == null) {
                m.put(num, 1);
            } else {
                m.put(num, existing + 1);
            }
        }

        for (Integer freq : m.values()) {
            if (freq >= 2) {
                count++;
            }
        }

        return count;
    }
}
