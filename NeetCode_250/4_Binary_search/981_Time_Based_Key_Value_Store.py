"""
Pattern: Hashmap plus Binary Search on a sorted history Problem

Invariant: Looking for the timestamp <= target, not just equal to the target
this means, binary search boundary problem, searching for the rightmost valid timestamp

Normal BS asks: Does target exist?

This problem:
Where is the boundary between valid and too large?

left represetns where target should be inserted
right respresents the last valid timestamp

In historical lookup problems, pay attention to whether the query wants
- exactly equal, less than or equal, or greater than or equal

- this determines the binary search boundary
"""



from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list) # key: [(value: timestamp)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.dict[key].append( (value, timestamp) )
   
    def get(self, key: str, timestamp: int) -> str:

        l = self.dict[key] # list of (value, timestamp)

        left = 0
        r = len(l) - 1

        # search space is the timestamps, if the timestamp is not there return the largest
        # else ""

        while left <= r:

            m = (left + r) // 2

            if l[m][1] == timestamp:
                return l[m][0]

            elif l[m][1] > timestamp:
                r = m - 1
            elif l[m][1] < timestamp:
                left = m + 1

        if r < 0:
            return ""
        
        return l[r][0]


if __name__ == "__main__":
    time_map = TimeMap()

    time_map.set("love", "high", 10)
    time_map.set("love", "low", 20)

    t1 = time_map.get("love", 5)
    t2 = time_map.get("love", 10)
    t3 = time_map.get("love", 15)
    t4 = time_map.get("love", 20)
    t5 = time_map.get("love", 25)

    print(t1)  # ""
    print(t2)  # "high"
    print(t3)  # "high"
    print(t4)  # "low"
    print(t5)  # "low"

"""
["TimeMap","set","set","get","get","get","get","get"]
[[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

"""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


