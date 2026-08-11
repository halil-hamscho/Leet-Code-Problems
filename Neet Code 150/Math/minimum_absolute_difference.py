class Solution:
    def minimumAbsDifference(self, arr):
        # Time Complexity: O (n log n) because we are sorting
        # Space Complexity: O (n) since worst case we can have the whole arr be an ans
        # Same time Complexity as the two loop one
        result = []
        arr.sort() # or arr = sorted(arr)
        min_abs = arr[1] - arr[0]
        for i in range(len(arr) - 1): # -1 since we do not want error by 1
            curr_abs = abs(arr[i + 1] - arr[i])
            if curr_abs < min_abs:
                min_abs = curr_abs
                result.clear()
                result.append([arr[i], arr[i + 1]])

            elif curr_abs == min_abs:
                result.append([arr[i], arr[i + 1]])
        return result



        # Two For Loop Solution
        # arr = sorted(arr) # lowest to highest
        # min_diff = arr[1] - arr[0]
        # result = []
        # for i in range(len(arr) - 1):
        #     curr_diff = arr[i + 1] - arr[i]
        #     if  curr_diff < min_diff:
        #         min_diff = min(min_diff, curr_diff)
        # for i in range(len(arr - 1)):
        #     if  arr[i + 1] - arr[i] == min_diff:
        #         result.append([arr[i], arr[i + 1]])
        # return result


def main():
    x = [4,2,1,3]
    result = Solution()
    print(result.minimumAbsDifference(x))

if __name__ == "__main__":
    main()