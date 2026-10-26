class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        result = 0
        l_val = height[l]
        r_val = height[r]

        while l < r:
            if l_val < r_val:
                l+= 1
                if height[l] > l_val:
                    l_val = height[l]
                else:
                    result += l_val - height[l]
                
            else:
                r-= 1
                if height[r] > r_val:
                    r_val = height[r]
                else:
                    result += r_val - height[r]
        return result
                
            
