class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        pre = 1
        for num_e in nums:
            prefix.append(pre * num_e)
            pre = pre * num_e
        post = 1
        postfix = [1] * len(nums)
        for num_o in range(len(nums) -1, -1, -1):
            postfix[num_o] = (post * nums[num_o])
            post = post * nums[num_o]
        
        result = []
        for idx in range(len(nums)):
            if idx - 1 < 0:
                result.append(1 * postfix[idx + 1])
            elif idx + 1 > (len(nums) - 1):
                result.append(prefix[idx - 1] * 1)
            else:
                result.append(prefix[idx - 1] * postfix[idx + 1])
        return result

            

        
        


            