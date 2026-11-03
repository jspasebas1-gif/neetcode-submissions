class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        result = []

        pre = 1
        for val in nums:
            prefix.append(pre * val)
            pre = pre * val
        post = 1
        postfix = [1] * len(nums)
        for idx in range(len(nums) -1,-1,-1):
            postfix[idx] = (post * nums[idx])
            post = postfix[idx]
        for idx2 in range(len(nums)):
            if idx2 == 0:
                nums[idx2] = (1 * postfix[idx2 + 1])
            elif idx2 == (len(nums) - 1):
                nums[idx2] = (prefix[idx2 - 1] * 1)
            else:
                nums[idx2] = (prefix[idx2 - 1] * postfix[idx2 + 1])

        return nums 

