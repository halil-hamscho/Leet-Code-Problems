class Solution:
    def merge(self, intervals):
        i = 0
        intervals = sorted(intervals, key=lambda x: x[0])
        resulting_array = []
        while i < len(intervals) - 1:
            a, b = intervals[i]
            c, d = intervals[i + 1]
            # Overlapping Intervals
            if max(a, c)  <= min(b, d):
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i, [min(a,b,c,d), max(a,b,c,d)])
            else: # Non Overlapping
                i += 1
        return intervals
    def merge_2(self, intervals):
        intervals.sort(key = lambda x : x[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            # Overlapping
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(end, lastEnd) # Edge Case: [1, 5], [2, 4]
            # No Overlapping
            else:
                output.append([start, end])
        return output

            
def main():
    result = Solution()
    print(result.merge([[1,3],[2,6],[8,10],[15,18]]))

if __name__ == "__main__":
    main()

        