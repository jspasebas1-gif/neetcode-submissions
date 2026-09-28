class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prev = 1
        for prenum in nums:
            prefix.append(prenum * prev)
            prev *= prenum
        postfix = [1] * len(nums)
        post = 1
        for prenum in range(len(nums) -1, -1, -1):
            postfix[prenum] = (nums[prenum] * post)
            post *= nums[prenum]
        for idx in range(len(nums)):
            if idx - 1 < 0:
                nums[idx] = 1 * postfix[idx + 1]
            elif idx + 1 > len(nums) - 1:
                nums[idx] = prefix[idx - 1] * 1
            else:
                nums[idx] = prefix[idx - 1] * postfix[idx + 1]
        return nums
                