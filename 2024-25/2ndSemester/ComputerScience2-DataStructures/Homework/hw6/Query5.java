// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.hw;

import java.io.IOException;
import java.util.Collections;
import java.util.Map;
import java.util.TreeMap;

public class Query5 {
    public static String Query5(Iterable<FlightRecord> input) {
        Map<Integer, Integer> m = new TreeMap<>();
        int mostFlights = 0;
        int month = 0;
        // count flights per month
        for (FlightRecord r : input){
            if(m.containsKey(r.MONTH)) {
                m.put(r.MONTH, m.get(r.MONTH)+1);
            }else {
                m.put(r.MONTH, 1);
            }
            // update most flights month
            if(m.get(r.MONTH) > mostFlights) {
                month = r.MONTH;
                mostFlights = m.get(r.MONTH);
            }

        }
        return(month + " had " + mostFlights + " flights");
    }
        // replace with your implementation


    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights/flights1990.csv");
        String r = Query5(input);
        System.out.println(r);
    }
}
