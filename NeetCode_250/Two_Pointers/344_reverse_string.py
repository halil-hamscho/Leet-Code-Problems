class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        i = 0
        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]

            i += 1
            j -= i



if __name__ == "__main__":
    s = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
    result = Solution().reverseString(s)