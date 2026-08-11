class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Edge Case
        if t == "": return ""
        
        countT, window = {}, {}

        # Frequency Map
        countT= {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        have, need = 0, len(countT)
        res, result_length = [-1,-1], float("infinity")
        l = 0
        for r in range(len(s)):
            '''
            Logic here is that we need to return the minimum window substring
            '''
            char = s[r]
            window[char] = 1 + window.get(char, 0)
            # Does window == countT
            if (char in countT) and window[char] == countT[char]:
                have += 1 # satisfied a condition

            while have == need:
                # update the result potentially
                if (r - l + 1) < result_length: 
                    res = [l, r]
                    result_length = (r - l + 1)
                # pop from the left of our window
                window[s[l]] -= 1 # since we removed a character our conditon can
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if result_length != float("infinity") else ""
    
def main():
    print()
    t = "ABC"
    s = "ADOBECODEBANC"
    test = Solution()
    print(test.minWindow(s,t))

if __name__ == "__main__":
    main()