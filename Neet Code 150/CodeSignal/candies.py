def solution(n,m):
    if n == 0:
        return 0
    return (m // n) * n

def main():
    print(solution(3,10))

if __name__ == "__main__":
    main()