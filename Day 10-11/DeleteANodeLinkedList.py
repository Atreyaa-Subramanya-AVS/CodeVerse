class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        Deletes a node from a singly linked list, given only access to that node.
        """
        node.val = node.next.val
        node.next = node.next.next

def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def find_node(head, value):
    while head and head.val != value:
        head = head.next
    return head

values = [4, 5, 1, 9]
head = create_linked_list(values)

node_to_delete = find_node(head, 5)

Solution().deleteNode(node_to_delete)

print(linked_list_to_list(head))
