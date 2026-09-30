# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        stack = []
        stack.append((root, root.val))
        
        while stack:
            curr, high = stack.pop()
            if curr.val >= high:
                count += 1
            highNew = max(curr.val, high)
            if curr.right:
                stack.append((curr.right, highNew))
            if curr.left:
                stack.append((curr.left, highNew))
        return count
        