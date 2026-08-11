'''
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

OKay so basically what happens is
they give us numbers
and we just simply have to count the numbers in between

Output the minimal number of statues
tat need to be added to existing statues
such thatit contains every integer
size from an interval [L, r]
[3 - 2] 

'''

def solution(statues):
    print(f"Before Sorting {statues}")
    statues = sorted(statues)
    print(f"After Sorting {statues}")

    l, r = 0,0
    res = 0
    while r < len(statues) - 1:
        r += 1
        interval = statues[r] - statues[l]
        if interval != 1:
            res += interval - 1
        l += 1
    return res

def main():
    print(solution([6,2,3,8]))

if __name__ == "__main__":
    main()
            
        



def main():
    print(solution([6,2,3,8]))

if __name__ == "__main__":
    main()
