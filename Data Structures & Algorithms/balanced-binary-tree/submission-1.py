# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return [True, 0]
            hl, hr = dfs(node.left), dfs(node.right)
            result = hl[0] and hr[0] and (abs(hl[1] - hr[1])) <= 1
            return [result, 1 + max(hl[1], hr[1])]
        return dfs(root)[0]
       


        