class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        temp = []

        i = 0
        j = 0
        while i < len(word1) or j < len(word2):

            if i >= len(word1):
                temp.append(word2[j:])
                return "".join(temp)

            if j >= len(word2):
                temp.append(word1[i:])
                return "".join(temp)

            temp.append(word1[i])
            temp.append(word2[j])

            i += 1
            j += 1

        return "".join(temp)

        


if __name__ == "__main__":
    word1 = "abc" 
    word2 = "pq"
    result = Solution().mergeAlternately(word1, word2)