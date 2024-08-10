class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def same(node,data):
            if not node:
                return True
            if node.val != data:
                return False
            return same(node.left,data) and same(node.right,data)
        return same(root,root.val)
         
