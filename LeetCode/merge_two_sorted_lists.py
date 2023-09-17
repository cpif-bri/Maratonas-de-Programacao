# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
        dummy_head = ListNode()
        current = dummy_head

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If one of the lists is exhausted, append the remaining elements of the other list
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2

        return dummy_head.next

# Inicialize a primeira lista
lista1 = ListNode(1)
lista1.next = ListNode(2)
lista1.next.next = ListNode(3)

# Inicialize a segunda lista
lista2 = ListNode(4)
lista2.next = ListNode(5)
lista2.next.next = ListNode(6)

listF = Solution.mergeTwoLists(list1=lista1, list2=lista2)

print('')

while listF != None:
            print(listF.val)
            listF = listF.next
