'''
Design an algorithm to encode a list of strings
to a single string

The encoded string is then decoded back to the original list of strings


- The trick here is to utilize a useful delimiter
- in this case, I will should not use a specific delimiter
- this is because if the delimiter appears on a part of the string
- then the input and output will not work


The trick is to remember the length of each word as you move
through out the array

- we cannot create a new data structure, we should utilize only
the encode and decode

IDEA: based on the length of each word, include that number
in the front of the word

'''




class Solution:

    def encode(self, strs) -> str:

        result = '' # encoding the string
        for s in strs:
            # len + delimiter + actual string
            result += str(len(s)) + '#' + s # (4#neet)

        return result

        # if len(strs) == 0:
        #     return '[]'
        # # utilize a unique separator
        # encoding = '-'.join(['EMPTY' if element == '' else str(element) for element in strs])
        # return encoding

    def decode(self, s):

        # now given a single encoded string
        result = []
        # number pointer initialization
        number_pointer = 0

        while number_pointer < len(s): # we do this to keep the pointer in bounds
            # first position is the integer, find the delimiter
            delimiter_pointer = number_pointer
            # each loop reads one word
            while s[delimiter_pointer] != '#':
                # keep incrementing until you get to the pound character
                delimiter_pointer += 1
                # tell us how many cahracters we have to read
            length = int(s[number_pointer:delimiter_pointer])
            result.append(s[delimiter_pointer + 1 : delimiter_pointer + 1 + length])
            number_pointer = delimiter_pointer + 1 + length
        return result




        # if s == '[]':
        #     return []
        # # split the special case
        # decoding = ['' if element == 'EMPTY' else element for element in s.split('-')]
        # return decoding


def main():
    print()
    test = Solution()
    input = ['halil', 'hamscho']
    encoding = test.encode(input)
    print(encoding)
    print(test.decode(encoding))


if __name__ == '__main__':
    main()