'''
a 1 interesting polygon is just a square with a side of length 1
an n interesting polygon is obtaine dby taking the n - 1 
interesting polygoin and apending 1 interesting

okay so let's say I get like n = 2
so for 

teh sides are 4 X n - 1
so lets say n 

Okay so we can add this from the bottom up


'''
def solution(n):
    result = 0
    print(f"Current N {n}")
    if n == 0:
        return 0
    for index in range(n):
        # index is technically n - 1
        print(f"Current Index {index}")
        if index == 0:
            result += 1
        else:
            result += 4 * (index)
        print(f"Current Result {result}")
    return result

def main():
    print(solution(3))

if __name__ == "__main__":
    main()


