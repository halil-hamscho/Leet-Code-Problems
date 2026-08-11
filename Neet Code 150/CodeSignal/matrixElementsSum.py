'''
Refuse to stay in any of the free rooms
or any of the rooms below any of the free rooms

Given a matrix, a rectangular matrix of integers
where each value represents the cost
of the room, your task is to return the total
sum of all rooms that are suitable for the
CodeBots

ADD UP ALL THE VALUES THAT DON'T APPEAR BELOW a 0

'''

def solution(matrix):
    res = 0
    bad_columns = []
    for idxI, arrayI in enumerate(matrix):
        print(f"Current Row Index: {idxI}")
        for idxJ, arrayJ in enumerate(arrayI):
            print(f"Current Column Index: {idxJ}")
            print(f"Current Value: {arrayJ}")
            # if the value I am in right now is not 0 and the the top value is not 0
            if arrayJ == 0:
                # if it equals to 0, we want to not add any values in this column
                bad_columns.append(idxJ)
            elif idxI == 0 and arrayJ != 0:
                print("No previous row exists")
                print(f"adding value {arrayJ}")
                res += arrayJ
            elif idxJ in bad_columns:
                continue
            else:
                res += arrayJ
    return res


def main():
    matrix = [[1,0,3],
              [0,2,1],
              [1,2,0]]
    print(solution(matrix))

if __name__ == "__main__":
    main()