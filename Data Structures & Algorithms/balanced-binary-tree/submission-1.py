# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return root == None or (abs(self.height(root.right) - self.height(root.left)) <= 1 and self.isBalanced(root.right) and self.isBalanced(root.left))

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else: return 1 + max(self.height(root.right), self.height(root.left))