# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def inorder(node):
            if not node:
                return False
            left = inorder(node.left)
            if isSame(node, subRoot):
                return True
            right = inorder(node.right)
            return left or right

        def isSame(l, r) -> bool:
            if not l or not r:
                return l == r

            if l.val != r.val:
                return False
            return isSame(l.left, r.left) and isSame(l.right, r.right)

        return inorder(root)
