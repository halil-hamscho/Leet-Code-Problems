'''
Given a sequence of integers as an array,
determine whether it is possible to
obtain a strictly increasing sequence by removing no more
than one element from an array

if it is 1,1,1 and we remove one 1 then it is still cooked
since 1 -> 1 is not 

 can only remove one elemen
'''

def solution(sequence):
    removed = 0
    previous_maximum = maximum = float('-infinity')
    for s in sequence:
        if s > maximum:
            # All good
            previous_maximum = maximum
            maximum = s
        elif s > previous_maximum:
            # Violation - remove current maximum outlier
            removed += 1
            maximum = s
        else:
            # Violation - remove current item outlier
            removed += 1
        if removed > 1:
            return False
    return True

def main():
    print(solution([1, 3, 2,1,1]))

if __name__ == "__main__":
    main()