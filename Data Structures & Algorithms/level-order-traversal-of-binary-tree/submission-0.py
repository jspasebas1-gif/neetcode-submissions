# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        
        queue = deque()
        queue.append(root)
        
        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(level)
        return result



        

        