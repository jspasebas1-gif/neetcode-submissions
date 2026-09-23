class Solution:
    # Count repetition into set/dict Value: # repeated
    # Initialize new array with empty arrays, size = len
    # Use set to add to arrays
    # From bottom up find k most frequent elements

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amount = {}
        total = [[] for _ in range(len(nums) + 1)] 
        result = []
        for num in nums:
            amount[num] = 1 + amount.get(num, 0)
        for value, repeat in amount.items():
            total[repeat].append(value)
        for item in range(len(total) -1, 0, -1):
            for freq in total[item]:
                result.append(freq)
                if len(result) == k:
                    return result
            

        
        

        