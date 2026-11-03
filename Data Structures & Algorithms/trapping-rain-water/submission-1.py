class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_val = height[l]
        r_val = height[r]
        result = 0
        while l < r:
            if l_val < r_val:
                l+=1
                if l_val < height[l]:
                    l_val = height[l]
                else:
                    result += l_val - height[l]
            else:
                r-=1
                if r_val < height[r]:
                    r_val = height[r]
                else:
                    result += r_val - height[r]
        return result