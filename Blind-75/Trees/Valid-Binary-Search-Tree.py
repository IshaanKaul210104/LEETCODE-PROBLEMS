# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvalid(node, minn, maxx) -> bool:
            if not node:
                return True
            if node.val >= maxx or node.val <= minn:
                return False

            left = isvalid(node.left, minn, node.val)
            right = isvalid(node.right, node.val, maxx)

            return left and right

        return isvalid(root, -1001, 1001)
