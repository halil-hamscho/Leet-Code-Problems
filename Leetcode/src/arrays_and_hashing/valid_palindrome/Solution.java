package arrays_and_hashing.valid_palindrome;

public class Solution {
    public boolean isPalindrome(String s) {
        // String Builder Approach
        StringBuilder builder = new StringBuilder();

        char[] charArray = s.toCharArray();

        for (char ch : charArray) {
            if (Character.isLetterOrDigit(ch)) {
                builder.append(Character.toLowerCase(ch));
            }
        }
        String filteredString = builder.toString();
        String reversedString = builder.reverse().toString();

        if (filteredString.equals(reversedString)) return true;
        return false;
    }
    public boolean isPalindrome_2(String s) {
        // first remove all non-alphanumeric values
        StringBuilder string  = new StringBuilder();

        char[] charArray = s.toCharArray();
        for (char ch: charArray) {
            if (Character.isLetterOrDigit(ch)) {
                // We want to append the lower case of this character
                string.append(Character.toLowerCase(ch));
            }
        }
        // String full of only alphanumeric numbers
        int l = 0;
        int r = string.length() - 1;
        while (l <= r) {
            if (string.charAt(l) != string.charAt(r)) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    // return f(s, 0); if we want to do the recursive solution
    private boolean f(String s, int i) {
        if (i >= s.length() / 2) return true;
        if (s.charAt(i) != s.charAt(s.length() - i - 1)) return false;
        return f(s, i + 1);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String s = "A man, a plan, a canal: Panama";
        System.out.println(sol.isPalindrome_2(s));
    }
}
