class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
         #visited set num: sequence value
         #current.get(num, 1)
         #while current - 1 in visited: iterate
         
         visited = set(nums)
         if not visited:
            return 0
         result = 1
         for num in nums:
            if num - 1 not in visited and num + 1 in visited:
                count = 1
                while num + 1 in visited:
                    num += 1
                    count += 1
                if count > result:
                    result = count
         return result


