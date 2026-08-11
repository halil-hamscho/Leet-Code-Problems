'''
Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Use a built in data structure 

'''
class MinStack:
    # constructor
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if there is already a value already in the minStack, we need the min of those two
        if self.minStack:
            val = min(val, self.minStack[-1])
            self.minStack.append(val)
        else:
            self.minStack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] #[-1] gets the last value
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
def main():
    print()
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    obj.getMin()
    obj.pop()
    obj.top()
    obj.getMin()

if __name__ == "__main__":
    main()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()