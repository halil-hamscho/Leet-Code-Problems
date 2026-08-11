package arrays_and_hashing.search_suggestions_system;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        // Sort the Products in lexicographic order
        Arrays.sort(products);
        int left = 0;
        int right = products.length - 1;
        List<List<String>> main_result = new ArrayList<>();

        for (int i = 0; i < searchWord.length(); i++) {

            // Get our Window of Correct Product Words
            while (left <= right && (i >= products[left].length() || products[left].charAt(i) != searchWord.charAt(i))) {
                left++;
            }
            while (left <= right && (i >= products[right].length() || products[right].charAt(i) != searchWord.charAt(i))) {
                right--;
            }
            // Got our window
            List<String> currentSuggestions = new ArrayList<>();
            int window = right - left + 1;
            // Add suggestions up to the min of 3 or the window
            for (int j = 0; j < Math.min(3, window); j++) {
                // Populate the list with the suggestions
                currentSuggestions.add(products[left + j]);
            }
            // Add the list to 2D Array
            main_result.add(currentSuggestions);
        }
        return main_result;
    }
}
