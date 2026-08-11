def solution(n):
    res = 0
    to_string = str(n)
    for number in to_string:
        print(number)
        res += int(number)
    return res




def main():
    print(solution(29))

if __name__ == "__main__":
    main()