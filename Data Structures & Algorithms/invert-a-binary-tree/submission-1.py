# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: return None
        tmp1 = self.invertTree(root.right)
        tmp2 = self.invertTree(root.left)
        return TreeNode(root.val, tmp1, tmp2)