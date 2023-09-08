# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ''
        s2 = ''

        while l1:
            s1 = s1 + str(l1.val)
            l1 = l1.next

        while l2:
            s2 = s2 + str(l2.val)
            l2 = l2.next

        result = str(int(s1[::-1]) + int(s2[::-1]))[::-1]

        dummy = ListNode(0)
        current = dummy

        for s in result:
            current.next = ListNode(int(s))
            current = current.next

        return dummy.next


# Create ListNode objects for the input numbers
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution.addTwoNumbers(l1, l2)
# Traverse the result linked list and print its values
while result:
    print(result.val, end=" ")
    result = result.next
        


