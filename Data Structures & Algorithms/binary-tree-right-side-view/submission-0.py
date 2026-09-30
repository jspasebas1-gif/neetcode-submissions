# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            level_r = []
            for _ in range(level_size):
                curr = queue.popleft()
                level_r.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(level_r[-1])
        return result

            
         
        