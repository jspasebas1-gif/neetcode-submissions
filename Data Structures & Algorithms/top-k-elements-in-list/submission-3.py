class Solution:
    # Count repetition into set/dict Value: # repeated
    # Initialize new array with empty arrays, size = len
    # Use set to add to arrays
    # From bottom up find k most frequent elements

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amount = {}
        bucket = [[] for _ in range(len(nums)+ 1)]
        result = []
        for value in nums:
            amount[value] = 1 + amount.get(value, 0)
        for key, v in amount.items():
            bucket[v].append(key)
        for rep in range(len(bucket) -1, 0, -1):
            for item in bucket[rep]:
                result.append(item)
                if len(result) == k:

                    return result
        

        