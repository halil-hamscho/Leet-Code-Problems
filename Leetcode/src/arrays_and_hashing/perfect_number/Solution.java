package arrays_and_hashing.perfect_number;

public class Solution {
    public boolean checkPerfectNumber(int num) {
        // iterate from 1 to num - 1
        int result = 0;
        for (int i = 1; i <= num - 1; i++) {
            // Only add divisors that divide num evenly
            // if we divide num by a divisor and if its remainer is 0
            System.out.println("i " + i);
            System.out.println("num / i " + (num / i));
            if  (num % i == 0) {
                // Even
                result += i;
                System.out.println("result " + result);
            }
        }
        if (result == num) {
            return true;
        }
        return false;
    }

    public static void main (String[] args) {
        Solution sol = new Solution();
        int n = 28;
        System.out.println(sol.checkPerfectNumber(n));
    }
}
