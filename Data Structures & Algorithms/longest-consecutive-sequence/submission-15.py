class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = set(nums)
        result = 0
        if not nums:
            return 0
        

        for num in nums:
            if num + 1 in new and num - 1 not in new:
                count = 1
                while num + count in new:
                    count += 1
                    
                result = max(result, count)
        if result == 0:
            return 1
        return result

 