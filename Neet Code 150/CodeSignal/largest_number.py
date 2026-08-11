def solution(n):
    str = ""
    if n == 0:
        return 0
    else:
        for value in range(n): # for n = 2 it will be 0, 1
            str = str + "9"
    return int(str)
            

def main():
    print(solution(2))

if __name__ == "__main__":
    main()