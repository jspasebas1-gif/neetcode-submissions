# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return []
        
        result = []
        stack = []
        stack.append((root, root.val))
        result.append(root)
        while stack:
            curr, val = stack.pop()
            if curr.val >= val:
                result.append(curr)
            nVal = max(curr.val, val)
            if curr.left:
                stack.append((curr.left, nVal))
            if curr.right:
                stack.append((curr.right, nVal))
        return len(result) - 1
             