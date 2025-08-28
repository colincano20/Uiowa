// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.hw;

import java.io.IOException;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.*;

public class Query9 {
    public static Iterable<String> Query9(Iterable<FlightRecord> input) {
        Map<String, Map<String, Integer>> m = new TreeMap<>();
        // build nested maps
        for (FlightRecord r : input) {
            String dest = r.DEST_STATE_ABR;
            String airline = r.UNIQUE_CARRIER_NAME;

            m.putIfAbsent(dest, new HashMap<>());
            Map<String, Integer> m2 = m.get(dest);
            m2.put(airline, m2.getOrDefault(airline, 0) + 1);
        }
        List<String> results = new ArrayList<>();
        // find the airline with most flights into each state
        for (String state : m.keySet()) {
            Map<String, Integer> m3 = m.get(state);
            String carrier = "";
            int maxFlights = -1;
            for (Map.Entry<String, Integer> entry : m3.entrySet()) {
                if (entry.getValue() > maxFlights) {
                    carrier = entry.getKey();
                    maxFlights = entry.getValue();
                }
            }
            results.add(state + "," + carrier);
        }
        return results;
    }

    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights/flights2005.csv");
        Iterable<String> rs = Query9(input);
        for (String r : rs) {
            System.out.println(r);
        }
    }
}
