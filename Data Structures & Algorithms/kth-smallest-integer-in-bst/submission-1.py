# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ct = 0
        self.res = None

        def inOrder(root,k):
            if root is None:
                return
            inOrder(root.left, k)
            self.ct += 1
            if self.ct == k:
                self.res = root.val
            inOrder(root.right, k)
        inOrder(root, k)
        return self.res
