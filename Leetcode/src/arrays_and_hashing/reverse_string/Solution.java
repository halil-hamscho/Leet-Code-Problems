package arrays_and_hashing.reverse_string;

public class Solution {
    public static void swap(char[] arr, int i, int j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public void reverseString(char[] s) {
        // Modify in place with O(1) extra memory
        // Two Pointer Approach?
        int l = 0;
        int r = s.length - 1;
        System.out.println("Before Swap: " + String.valueOf(s));
        while (l <= r) {
            System.out.printf("l (%d) r (%d) %n", l, r);
            swap(s, l, r);
            l++;
            r--;
        }
        System.out.println("After Swap: " + String.valueOf(s));
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        char[] s = {'h','e','l','l','o'};
        sol.reverseString(s);

    }
}
