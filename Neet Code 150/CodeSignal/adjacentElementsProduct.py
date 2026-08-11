def solution(inputArray):
    # given an array of integers, find the pair of adjacent elements
    # have to be adjacent so pointers
    curr_max = float("-inf")
    l, r = 0, 0
    while r != len(inputArray) - 1:
        r += 1
        print(f"New Right Pointer {inputArray[r]}")
        curr_max = max(curr_max, inputArray[l] * inputArray[r])
        print(curr_max)
        l += 1
        print(f"New Left Number {inputArray[l]}")
    return curr_max

def main():
    print(solution([-23, 4, -3, 8, -12]))

if __name__ == "__main__":
    main()


