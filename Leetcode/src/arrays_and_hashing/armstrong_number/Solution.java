package arrays_and_hashing.armstrong_number;

public class Solution {
    public boolean isArmstrong(int n) {
        double comp = n;
        // obtain the kth power
        // iterate through the digits and keep a result variable
        int k = String.valueOf(n).length();
        System.out.println("Current k" + k);
        double result = 0;
        while (n != 0) {
            int digit = n % 10; // Left most Digit
            System.out.println("Current leftmost digit: " + digit);
            result += Math.pow(digit, k);
            System.out.println("Current Result: " + result);
            n = n / 10;
            System.out.println("Current n: " + n);
        }
        if ( comp == result) {
            return true;
        }
        return false;
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        int n = 153;
        System.out.println(sol.isArmstrong(n));
    }
}
