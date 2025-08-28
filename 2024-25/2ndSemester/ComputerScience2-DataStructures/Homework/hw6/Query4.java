// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.hw;

import java.io.IOException;

import java.util.*;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Query4 {

    public static Iterable<String> Query4(Iterable<FlightRecord> input) {
        Set<String> s = new HashSet<>();

        Map<String, Integer> m = new TreeMap<>();
        // count number of flights to each destination from CID
        for (FlightRecord r : input){
            if(r.ORIGIN.equals("CID")) {
                // add to counter if flight exists
                if(m.containsKey(r.DEST)) {
                    m.put(r.DEST, m.get(r.DEST)+1);
                } else {
                    m.put(r.DEST, 1);
                }
            }
        }
        // format the results into strings
        for(FlightRecord r : input) {
            if(r.ORIGIN.equals("CID")) {
                s.add(r.DEST + "=" + m.get(r.DEST));
            }
        }

        return s;
    }

    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights/flights2005.csv");
        Iterable<String> results = Query4(input);

        for (String s : results) {
            System.out.println(s);
        }

    }
}
