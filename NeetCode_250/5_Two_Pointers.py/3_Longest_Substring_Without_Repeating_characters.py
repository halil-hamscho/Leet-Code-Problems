"""

The hint here is that we want the longest contigous substring satisfying a condition

Rather than restarting the sliding window every time, we can just repair it 
by removing an existing value from the left

Time: O(n) since it is O(n) + O(n) values can onyl be added and removed from the set once
Space: O(n)

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        st = set()
        l = 0
        result = 0

        for r in range(len(s)):

            while s[r] in st:
                st.remove(s[l])
                l += 1

            st.add(s[r])
            result = max(result, r - l + 1)

        return result

        

if __name__ == "__main__":
    result = Solution().lengthOfLongestSubstring("mq")