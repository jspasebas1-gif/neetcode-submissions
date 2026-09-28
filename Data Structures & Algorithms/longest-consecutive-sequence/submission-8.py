class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        visited = set(nums)
        result = 1
        for num in nums:
            if num + 1 in visited and num - 1 not in visited:
                count = 1
                while num + count in visited:
                    count += 1
                result = max(result, count)
        return result


         
      
