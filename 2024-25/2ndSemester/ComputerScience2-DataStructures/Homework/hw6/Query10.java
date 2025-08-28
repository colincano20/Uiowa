// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.hw;

import java.io.IOException;
import java.util.*;

public class Query10 {

    public static Iterable<String> Query10(Iterable<FlightRecord> input) {
        //set of all destinations from CID
        Set<String> s1 = new HashSet<>();
        //set of all origins with destination LAX
        Set<String> s2 = new HashSet<>();

        // build the sets
        for (FlightRecord r : input) {
            if (r.ORIGIN.equals("CID")) {
                s1.add(r.DEST);
            }
            if (r.DEST.equals("LAX")) {
                s2.add(r.ORIGIN);
            }
        }
        // Find intersection of 2 sets
        s1.retainAll(s2);
        List<String> results = new ArrayList<>();
        for (String layover : s1) {
            results.add("CID->" + layover + "->LAX");
        }
        //return intersection of 2 sets.
        return results;
    }

    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights/flights2020.csv");
        Timer t = new Timer();
        t.start();
        Iterable<String> results = Query10(input);
        t.end();
        for (String s : results) {
            System.out.println(s);
        }
        System.out.println(t.elapsedSeconds());
    }
}
