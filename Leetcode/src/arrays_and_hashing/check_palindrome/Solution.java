package arrays_and_hashing.check_palindrome;

public class Solution {
    public boolean isPalindrome(int x) {
        String s = String.valueOf(x);
        if (s.length() == 0 || s.length() == 1) {
            return true;
        }
        // Utilize 2 pointer approach
        // "ABC" l = 0 , r = 3 - 1 = 2
        int l = 0;
        int r = s.length() - 1;
        while (l <= r) {
            if (s.charAt(l) != s.charAt(r)) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        int variable = 121;
        boolean result = sol.isPalindrome(variable);
        System.out.println(result);
    }
}
