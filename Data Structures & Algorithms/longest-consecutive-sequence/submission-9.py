class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        visited = set(nums)
        result = 1

        for num in nums:
            if num + 1 in visited and num - 1 not in visited:
                point = 1
                while num + point in visited:
                    point += 1
                result = max(result, point)
        return result