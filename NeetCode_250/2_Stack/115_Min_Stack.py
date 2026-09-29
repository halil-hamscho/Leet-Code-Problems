class MinStack:

    def __init__(self):
        self.list = []
        self.low = None

    def push(self, value: int) -> None:

        if not self.list:
            self.low = value
            self.list.append( (value, self.low) )
            return

        if value < self.low:
            self.low = value

        self.list.append( (value, self.low ))
            
    def pop(self) -> None: # have to update self.low as well


        self.list.pop()
        if not self.list:
            self.low = None
        else:
            self.low = self.list[-1][1]


    def top(self) -> int: # Done

        return self.list[-1][0]

    def getMin(self) -> int: # Done

        return self.list[-1][1]



        
if __name__ == "__main__":
    result = MinStack()

    result.push(-10)
    result.push(14)

    print(result.getMin())   # expected: -10
    print(result.getMin())   # expected: -10

    result.push(-20)

    print(result.getMin())   # expected: -20
    print(result.getMin())   # expected: -20
    print(result.top())      # expected: -20
    print(result.getMin())   # expected: -20

    result.pop()

    result.push(10)
    result.push(-7)

    print(result.getMin())   # expected: -10

    result.push(-7)
    result.pop()

    print(result.top())      # expected: -7
    print(result.getMin())   # expected: -10

    result.pop()