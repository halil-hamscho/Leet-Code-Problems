
'''
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] 
is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. 
The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored 
(i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

Solution:
- We traverse pairs of position and speed in reverse order after sorting
- We do this because we want to calculate the time it will take for a car
to reach the target
- if a car is behind another and they have a smaller time, then this means
they will collide with the car in the front. 

we use a stack to keep track of the number of car fleets. 
If the car behind stack[-1] is < stack[-2] (time is less) pop the car behind (stack[-1])
and at the end the len of the stack is the number of car fleets

Zip Function: think of the zip in your jeans,
if you want to close your jeans, then you zip your pants up
If you want to join two lists, what we can do is use the zip function

pass two containers (list)
you can do 
zipped = dict(zip(names, companies))

or list(zip...)
or set(zip)
 '''
class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        stack = []
      # for every position & and speed in both position and speed lists, create pairs
        pairs = [[p,s] for p,s in zip(position, speed)]
      
        for p,s in sorted(pairs)[::-1]: # Reverse sorted order
        # if we get to a car, we need time = distance / velocity
            stack.append((target - p) / s) # decimal division
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

def main():
    print()
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    test = Solution()
    print(test.carFleet(target,position,speed))

if __name__ == '__main__':
    main()