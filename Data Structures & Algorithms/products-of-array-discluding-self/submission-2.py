class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        pre = 1
        for num_e in nums:
            prefix.append(num_e * pre)
            pre *= num_e
        postfix = [1] * len(nums)
        post = 1
        for num_o in range(len(nums) -1, -1, -1): #start, end, dec
            postfix[num_o] = nums[num_o] * post
            post = postfix[num_o]
        for num in range(len(nums)):
            if num - 1 < 0:
                nums[num] = 1 * postfix[num + 1]
            elif num + 1 > (len(nums) - 1):
                nums[num] = 1 * prefix[num - 1]
            else:
                nums[num] = prefix[num - 1] * postfix[num + 1]
        return nums
       