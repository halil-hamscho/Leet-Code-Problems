'''
Given a string seq that consits of  the characters "a" and 'b' only
in on emove, delete either an AB or a BB substring and concatenance the remaiuning substrings

Find the minimum possible length of the remaining string after performing any number of moves

We need to utilize a stack it is leetcode prolem 2696


'''

# def getMinLength(seq):
#     stack = []
#     for index, value in enumerate(seq):
#         if stack and ((stack[-1] == "A" and value == "B") or (stack[-1] == "B" and value == "B")):
#             stack.pop()
#         else:
#             stack.append(value)
#     return len(stack)

# def main():
#     print()
#     seq = "BABBA"
#     result = getMinLength(seq)
#     print(result)

# if __name__ == "__main__":
#     main()


'''
Alex and Chris are learning to infiltrate a secure system
Starting with a string of code, alex will remove any substring with an odd number of vowels
Chris then removes any substring from the remaining code with an even number of vowels. This learning
continues unitl one of them is unable to make a move
Given an array of n strings of code, determinet he winner of each round and report the reults as either "Alex or "Chris"
accorddingly

VOWELS: a e i o u



'''


def 