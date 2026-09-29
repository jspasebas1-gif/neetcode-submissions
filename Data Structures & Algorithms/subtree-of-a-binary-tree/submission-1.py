# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if root.val == subRoot.val:
            if self.sameTree(root, subRoot):
                return True
        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        else:
            return False


        


    def sameTree(self, root, subroot):
         if root is None and subroot is None:
            return True
         elif root is None or subroot is None:
            return False
         elif root.val != subroot.val:
             return False
         else:
             return self.sameTree(root.left, subroot.left) and self.sameTree(root.right, subroot.right)
            
