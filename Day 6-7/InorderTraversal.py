from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)

        inorder(root)
        return res

def build_tree():

    node3 = TreeNode(3)
    node2 = TreeNode(2, left=node3)
    root = TreeNode(1, right=node2)
    return root

if __name__ == "__main__":
    root = build_tree()
    solution = Solution()
    output = solution.inorderTraversal(root)
    print("Inorder Traversal:", output)
