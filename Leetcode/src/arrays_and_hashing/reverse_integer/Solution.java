package arrays_and_hashing.reverse_integer;

class Solution {
    public int reverse(int x) {
        int num = Math.abs(x);
        int rev = 0;
        while (num != 0) {
            int ld = num % 10;
            // Checks if adding the next digit to rev will cause an overflow beyond the integer limit
            if (rev > (Integer.MAX_VALUE - ld) / 10) {
                return 0;
            }
            rev = (rev * 10) + ld;
            num = num / 10; // update num
        }
        if (x < 0) {
            return (-rev);
        }
        else return rev;
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        int answer = sol.reverse(123);
        System.out.println(answer);
    }
}