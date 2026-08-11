
'''
I implemented it this way:
        for i in range(len(s)):
            if i == len(s) - 1:
                result += hashmap[s[i]]
            else:
                if s[i] ==  "I" and s[i + 1] in ("V", "X"):
                    result += (hashmap[s[i + 1]] - hashmap[s[i]]) - hashmap[s[i + 1]]
                elif s[i] ==  "X" and s[i + 1] in ("L", "C"):
                    result += (hashmap[s[i + 1]] - hashmap[s[i]]) - hashmap[s[i + 1]]
                elif s[i] ==  "C" and s[i + 1] in ("D", "M"):
                    result += (hashmap[s[i + 1]] - hashmap[s[i]]) - hashmap[s[i + 1]]
                else:
                    result += hashmap[s[i]]

However, we should use the numbers to our advantage where
if curr is < next then that means we are subtracting

'''
class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # Use Math to our Advantage
        # Iterate through the characters, if c < n, then c is negative
        # Read through string and compare adjacent values
        result = 0
        # iterating through the indices of the string
        # for i in range(len(s)):
        #     if i + 1 < len(s) and hashmap[s[i]] < hashmap[s[i + 1]]:
        #         # Not out of bounds and curr < next
        #         result -= hashmap[s[i]]
        #     else:
        #         result += hashmap[s[i]]
        # return result

        for index, roman in enumerate(s):
            if index + 1 < len(s) and hashmap[s[index]] < hashmap[s[index + 1]]:
                result -= hashmap[s[index]]
            else:
                result += hashmap[s[index]]
        return result


def main():

    # From 1 to 3999
    result = Solution()
    print(result.romanToInt("MCMXCIV"))

if __name__ == "__main__":
    main()