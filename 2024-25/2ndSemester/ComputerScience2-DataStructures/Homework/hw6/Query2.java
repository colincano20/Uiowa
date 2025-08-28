// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.hw;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Query2 {

    public static Iterable<String> Query2(Iterable<FlightRecord> input) {
        Set<String> s = new HashSet<>();
        // loop through all flight records
        for (FlightRecord r :input){
            // add destination and destination state abbreviation if origin is CID
            if (r.ORIGIN.equals("CID")){
                s.add(r.DEST +", "+ r.DEST_STATE_ABR);
            }
        }
        // return set of destinations from CID
        return s;
    }

    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights/flights2005.csv");
        Iterable<String> results = Query2(input);
        for (String s : results) {
            System.out.println(s);
        }
    }
}
