from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next

        return dummy.next

def print_list(head):
    while head:
        print(head.val, end=",")
        head = head.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
sol = Solution()
swapped = sol.swapPairs(head)
print_list(swapped)
