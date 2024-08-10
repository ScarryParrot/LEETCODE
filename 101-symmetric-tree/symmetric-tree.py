# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True  # An empty tree is symmetric

        def same(node, l, r):
            if l == None and r == None:
                return True
            if l == None or r == None:
                return False
            return l.val == r.val and same(node,l.left, r.right) and same(node,l.right, r.left)

        return same(root, root.left, root.right)
