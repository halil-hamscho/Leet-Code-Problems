package arrays_and_hashing.two_sum;

/*
Given an array of integers nums and an integer target, return indices of the two numbers such that
they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


1. Brute Force Solution O(n^2) we can try every single combination
2. Two Pass HashMap The first pass we populate the entire hashmap with the index and value
3. One pass hashmap
 */

/*
Streams API is a method that was introduced in java 8.
The streams API provides a powerful and modern way to process sequences of elements in a
declarative and functional style

 */

import java.util.ArrayList;
import java.util.HashMap;

public class Solution {
    public int[] twosum(int[] nums, int target ) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] ans = new int[2];
        // One Pass HashMap
        for (int i = 0; i < nums.length - 1; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                ans[0] = map.get(complement);
                ans[1] = i;
            }
            map.put(nums[i], i);
        }
        return ans;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {2,7,11,15};
        int target = 9;
        System.out.println(sol.twosum(nums, target));
    }
}
