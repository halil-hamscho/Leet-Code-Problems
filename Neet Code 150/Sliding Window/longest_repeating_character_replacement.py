'''
O(26n) Solution
#hashmap for the count for occurences
count = {}
res = 0

l = 0
# right pointer will be going through the entire string
for r in range(len(s)):
    # increase the count or set it equal to 0
    count[s[r]] = 1 + count.get(s[r],0)
    # <= or >
    while (r - l + 1) - max(count.values()) > k:
        count[s[l]] -= 1
        l += 1
    # r - l + 1 = size of window
    res = max(res, r - l + 1)
return res

'''





class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #hashmap for the count for occurences
        count = {}
        res = 0
       
        l = 0
        # If we keep track of the max frequency, we only switch the resule
        # if the maxf increases, so we do not have to look through the entire array
        maxf = 0
        # right pointer will be going through the entire string
        for r in range(len(s)):
            # increase the count or set it equal to 0
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(maxf, count[s[r]]) # when we add one, it can become the maxf
            # <= or >
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            # r - l + 1 = size of window
            res = max(res, r - l + 1)
        return res


def main():
    print()
    test = Solution()
    s = "ABAB"
    k = 2
    print(test.characterReplacement(s, k))

if __name__ == '__main__':
    main()