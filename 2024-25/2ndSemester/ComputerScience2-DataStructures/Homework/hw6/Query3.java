// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.hw;

import java.io.IOException;
import java.util.*;

public class Query3 {

    public static int Query3(Iterable<FlightRecord> input) {
        Set<String> s = new HashSet<>();
        int sum = 0;
        // build set of unique destinations from CID
        for (FlightRecord r :input){
            if (r.ORIGIN.equals("CID")){
                s.add(r.DEST +", "+ r.DEST_STATE_ABR);
            }
        }
        // return number of unique destinations
        return s.size();
    } // replace with your implementation



    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights/flights2020.csv");
        int results = Query3(input);
        System.out.println(results);
    }
}
