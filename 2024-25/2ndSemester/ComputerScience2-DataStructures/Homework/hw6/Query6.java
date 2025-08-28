// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.hw;

import java.io.IOException;
import java.util.Map;
import java.util.TreeMap;
import java.util.HashMap;

public class Query6 {
    public static String Query6(Iterable<FlightRecord> input) {
        Map<String, Integer> statePairs = new HashMap<>();
        String mostConnectedPair = "";
        int maxFlights = 0; // replace with your implemen
        for (FlightRecord r : input) {
            String state1 = r.ORIGIN_STATE_ABR;
            String state2 = r.DEST_STATE_ABR;



            // Sort states alphabetically so there is not any mismatches
            String pairKey;
            if (state1.compareTo(state2) < 0) {
                pairKey = state1 + "," + state2;
            } else {
                pairKey = state2 + "," + state1;
            }

            // count flights between state pairs
            statePairs.put(pairKey, statePairs.getOrDefault(pairKey, 0) + 1);

            // track the most common pair
            if (statePairs.get(pairKey) > maxFlights) {
                maxFlights = statePairs.get(pairKey);
                mostConnectedPair = pairKey;
            }
        }
        return "(" + mostConnectedPair + ")";
    }


    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights/flights1990.csv");
        String r = Query6(input);
        System.out.println(r);
    }
}
