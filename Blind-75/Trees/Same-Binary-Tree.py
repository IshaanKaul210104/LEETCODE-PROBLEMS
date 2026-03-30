# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(l, r) -> bool:
            if not l or not r:
                return l == r

            if l.val != r.val:
                return False
            return isSame(l.left, r.left) and isSame(l.right, r.right)

        return isSame(p, q)
