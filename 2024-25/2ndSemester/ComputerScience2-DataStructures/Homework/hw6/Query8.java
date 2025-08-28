// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.hw;

import java.io.IOException;
import java.text.DecimalFormat;
import java.util.*;

public class Query8 {
    public static Iterable<String> Query8(Iterable<FlightRecord> input) {
        Set<String> s = new HashSet<>();
        Map<String, Integer[]> m = new HashMap<>();
        // loop through flights to track total and intra-state flights
        for(FlightRecord r : input) {
            int temp = 0;
            if(r.ORIGIN_STATE_ABR.equals(r.DEST_STATE_ABR)) temp = 1;

            Integer[] i;
            if(m.containsKey(r.ORIGIN_STATE_ABR)) {
                i = m.get(r.ORIGIN_STATE_ABR);
                i[0] += temp;
                i[1] += 1;
            } else {
                i = new Integer[]{temp, 1};
            }
            m.put(r.ORIGIN_STATE_ABR, i);
        }
        String percent;
        DecimalFormat df = new DecimalFormat("#.000");

        // calculates the percentages for each state
        for(String j : m.keySet()) {
            percent = df.format((float) m.get(j)[0]/m.get(j)[1]);
            if(percent.equals(".000")) { continue; }
            s.add(j + "=" + percent);
        }

        return s;
    }

    public static void main(String[] args) throws IOException {
        Iterable<FlightRecord> input = DataImporter.getData("flights/flights2020.csv");
        Iterable<String> rs = Query8(input);
        for (String r : rs) {
            System.out.println(r);
        }

    }

}
