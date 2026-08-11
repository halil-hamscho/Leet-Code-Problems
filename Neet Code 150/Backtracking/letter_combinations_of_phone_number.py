class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return [] 
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }   
        res = []
        comb = ""
        def dfs(num, index, comb):
            if index >= len(num):
                res.append(comb)
                return
            for letter in digit_to_letters[num[index]]:
                comb = comb + letter
                dfs(num, index + 1, comb)
                comb = comb[:-1]
        dfs(digits, 0, comb)
        return res

def main():
    digits = ""
    result = Solution()
    print(result.letterCombinations(digits))

if __name__ == "__main__":
    main()
            