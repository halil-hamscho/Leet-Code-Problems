class TimeMap:

    def __init__(self):
        # key = string, value = list of [value, timestamp]
        self.store = {} # initialize hashmap
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # does the key exist
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = "" # if the key is not there
        # Check the list of values
        values = self.store.get(key, [])        
        # binary search
        left, right = 0, len(values) - 1
        while left <= right: # while the left pointer has not crossed the right pointer
            m = (left + right) // 2  #integer division
            if values[m][1] <= timestamp: 
                result = values[m][0]
                left = m + 1
            else:
                right = m - 1
                # we do not assign a result since it does not work
        return result

def main():
    print()
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1) 
    print(timeMap.get("foo", 1))
    print(timeMap.get("foo", 3))
    timeMap.set("foo", "bar2", 4)
    print(timeMap.get("foo", 4))
    print(timeMap.get("foo", 5))


if __name__ == '__main__':
    main()