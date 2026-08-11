package arrays_and_hashing.reformat_date;

import java.util.Arrays;
import java.util.HashMap;

public class Solution {
    public String reformatDate(String date) {
        // Intuition is to use a hashmap
        HashMap<String, String> map = new HashMap<>();
        map.put("Jan", "01");
        map.put("Feb", "02");
        map.put("Mar","03");
        map.put("Apr","04");
        map.put("May","05");
        map.put("Jun","06");
        map.put("Jul","07");
        map.put("Aug","08");
        map.put("Sep","09");
        map.put("Oct","10");
        map.put("Nov","11");
        map.put("Dec","12");
        // Create string arr by removing the white space
        String[] arr = date.split("\\s+");
        StringBuilder builder = new StringBuilder();

        // Add the year
        builder.append(arr[2]).append("-");
        // Add the month
        builder.append(map.get(arr[1])).append("-");

        String day = arr[0]; // 1 0 t h
        StringBuilder dayBuilder = new StringBuilder();

        for(int i = 0; i < day.length(); i++){
            char c = day.charAt(i);
            if (Character.isDigit(c)) {
                dayBuilder.append(c);
            }
        }
        // Add leading zero for a single-digit day
        if (dayBuilder.length() == 1) {
            builder.append("0").append(dayBuilder.toString());
        } else {
            builder.append(dayBuilder.toString());
        }
        return builder.toString();
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        String date = "20th Oct 2052";
        System.out.println(sol.reformatDate(date));
    }
}
