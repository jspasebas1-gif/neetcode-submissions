# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

            
        valid, minV, maxV = self.helper(root)
        return valid
    def remove(self, nums):
        return [x for x in nums if x is not None]
    def helper(self, root):
        if root is None:
            return True, None, None
        bstL, minL, maxL = self.helper(root.left)
        bstR, minR, maxR = self.helper(root.right)

        valid = (
    bstL
    and bstR
    and (maxL is None or maxL < root.val)
    and (minR is None or root.val < minR)
)
            
        minV = min(self.remove([minL, minR, root.val]))
        maxV = max(self.remove([maxL, maxR, root.val]))
        return valid, minV, maxV
                        
            