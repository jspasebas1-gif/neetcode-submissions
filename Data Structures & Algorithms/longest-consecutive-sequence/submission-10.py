class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        new = set(nums)
        result = 1

        for num in new:
            if num + 1 in new and num - 1 not in new:
                total = 1
                while num + total in new:
                    
                    total += 1
                result = max(result, total)
        return result
