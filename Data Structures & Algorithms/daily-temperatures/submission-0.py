class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for val in range(len(temperatures)):
            while stack and temperatures[val] > temperatures[stack[-1]]:
                res[stack[-1]] = val - stack[-1]
                stack.pop()
            
            stack.append(val)
        while stack:
            cur = stack.pop()
            res[cur] = 0
        return res
            

        
        