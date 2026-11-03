# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot and not root: return True
        if not subRoot or not root: return False
        if root.val == subRoot.val: return (self.isSubtree(root.right, subRoot.right) and self.isSubtree(root.left, subRoot.left)) or self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        elif root.val > subRoot.val: return False
        else: return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)