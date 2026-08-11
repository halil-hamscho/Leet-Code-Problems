import random

class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        result = val not in self.numMap # True if it is not in the map
        if result:
            self.numMap[val] = len(self.numList) # we get the length before we append to the array, that is why we do not get error by 1
            self.numList.append(val)
        return result
            
    def remove(self, val: int) -> bool:
        result = val in self.numMap # True if it is in map
        if result: # We are able to remove
            # Get Index from hashmap
            index = self.numMap[val]
            # Get last value
            lastVal = self.numList[-1]
            # Set last value to new index  in array (replace)
            self.numList[index] = lastVal
            # Remove last value
            self.numList.pop()
            # Update hashmap with new index
            self.numMap[lastVal] = index
            # Delete old value
            del self.numMap[val]
        return result

    def getRandom(self) -> int:
        return random.choice(self.numList)

def main():
    result = RandomizedSet()

if __name__ == "__main__":
    main()