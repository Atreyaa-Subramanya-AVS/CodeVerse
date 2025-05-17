from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

def create_ll(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_l_to_l(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example usage
values = [1, 2, 3, 4, 5]
head = create_ll(values)
solution = Solution()
reversed_head = solution.reverseList(head)
print(linked_l_to_l(reversed_head))