class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0

        for pos, val in enumerate(heights):
            start = pos
            while stack and val < stack[-1][1]:
                width = pos - stack[-1][0]
                area = width * stack[-1][1]
                start = stack.pop()[0]

                result = max(result, area)
            stack.append((start,val))
        while stack:
            width = len(heights) - stack[-1][0]
            area = width * stack[-1][1]
            stack.pop()
            result = max(result, area)
        return result



    
        

        