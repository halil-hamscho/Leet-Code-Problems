from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int) # element, counter
        self.groups = defaultdict(list)

        self.max = 0 # counter
        
    def push(self, val: int) -> None:

        self.freq[val] += 1 # increase frequency

        freq = self.freq[val]

        if freq > self.max:
            self.max = freq

        self.groups[freq].append(val)
        
    def pop(self) -> int:

        result = None

        result = self.groups[self.max].pop()

        self.freq[result] -= 1

        if not self.groups[self.max]:
            self.max -= 1

        return result

if __name__ == "__main__":
    result = FreqStack()

    result.push(4)
    result.push(0)
    result.push(9)
    result.push(3)
    result.push(4)
    result.push(2)

    print(result.pop())

    result.push(6)

    print(result.pop())

    result.push(1)

    print(result.pop())

    result.push(1)

    print(result.pop())

    result.push(4)

    print(result.pop())
    print(result.pop())
    print(result.pop())
    print(result.pop())
    print(result.pop())
    print(result.pop())