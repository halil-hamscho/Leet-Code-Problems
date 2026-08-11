'''
Because it is in reverse order, what we need to do is understand addition
We need val1, val2 and a carry

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Always start with a dummy node
        dummy = ListNode()
        current = dummy

        carry = 0
        while l1 or l2 or carry: # add them until they are null
            # first value = the first value in l1 or 0 if l1 is null
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            # add them together, remember the carry
            sum = val_1 + val_2 + carry

            # Ex. sum is 15, get the carry out
            '''
            When the sum of the digists exceeds 9
            sum % 10 gives the remainder when sum is divided by 10
            Ex. 12 % 10 = 2, this 2 is the digit that should be placed in the current node of the result of the linked list

            This helps us ensure that, because we are doing this in reverse order, we want to include the 2 first before the 1
            '''
            carry = sum // 10 # calculates the carry, Ex. 12//10 = 1
            sum = sum % 10 # calculates the curent digit to be stored
            current.next = ListNode(sum)

            # Update Pointers
            current = current.next

            # update list 1 and 2 pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            # remember edge case 8 + 7, l1 and l2 are null but carry is 1
        return dummy.next

def list_to_linked_list(numbers):
    dummy = ListNode()
    current = dummy
    for number in numbers:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def main():
    l1 = list_to_linked_list([2, 4, 3, 3])
    l2 = list_to_linked_list([5, 6, 4])
    test = Solution()
    result = test.addTwoNumbers(l1, l2)
    result_list = linked_list_to_list(result)
    print(result_list)



if __name__ == "__main__":
    main()