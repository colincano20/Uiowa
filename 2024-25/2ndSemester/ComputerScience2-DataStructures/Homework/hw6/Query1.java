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

public class Query1 {

    public static int Query1(Iterable<FlightRecord> input) {
        int sum = 0;
        // loop through all flight records
        for (FlightRecord r : input){
            //find any flight with CID origin and add to sum
            if(r.ORIGIN.equals("CID")){
                sum++;
            }
        }
        // return total flights from CID
        return sum;
    }

    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights/flights1990.csv");
        int total = Query1(input);
        System.out.println(total);
    }
}
