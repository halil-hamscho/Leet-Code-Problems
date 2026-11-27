"""
Palindromes can be solved using Dynamic Programming

Expand Around Center Approach

The Fundamental Intuition is that every palidrome has a center, and the characters on either side of that center must match

as long as s[left] == s[right], we continue expanding

2 Types of Palindromes:

    1. Odd Length: there is a single character at the center
        a, b, a

    2. Even Length: the center lies between two characters
        a, b, b, a

Connection to DP: 
    a larger substring is a palindrome if its inner substring is a palindrome
    and its two outer characters match
"""