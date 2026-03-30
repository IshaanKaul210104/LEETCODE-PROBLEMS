# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        def inorder(node) -> None:
            if not node:
                return
            inorder(node.left)
            if len(heap) < k:
                heapq.heappush(heap, -node.val)
            else:
                if node.val < -heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, -node.val)
            inorder(node.right)

        inorder(root)
        return -heap[0]
