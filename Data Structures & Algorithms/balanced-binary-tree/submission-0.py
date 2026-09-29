# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.balance(root)[0]


    def balance(self, node):
        if not node:
            return [True, 0]
        heightl, heightr = self.balance(node.left), self.balance(node.right)
        result = heightl[0] and heightr[0] and (abs(heightl[1] - heightr[1]) <= 1)
        return [result, 1 + max(heightl[1], heightr[1])]
        
        


        