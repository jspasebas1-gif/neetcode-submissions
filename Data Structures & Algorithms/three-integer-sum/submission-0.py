class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        result = []

        for first in range(len(nums)):
            l, r = first + 1, len(nums) - 1
            while l < r:
                if (nums[first] + nums[l] + nums[r]) > 0:
                    r -= 1
                elif (nums[first] + nums[l] + nums[r]) < 0:
                    l += 1
                else:
                    value = [nums[first],nums[l],nums[r]]
                    if value not in result:
                        result.append([nums[first],nums[l],nums[r]])
                        l += 1
                        r -= 1
                    else:
                        l += 1
                        r -= 1
        return result


        