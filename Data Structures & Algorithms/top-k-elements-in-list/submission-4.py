class Solution:
    # Count repetition into set/dict Value: # repeated
    # Initialize new array with empty arrays, size = len
    # Use set to add to arrays
    # From bottom up find k most frequent elements

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        result = []
        for num in nums:
            if num in group:
                group[num] += 1
            else:
                group[num] = 1
        for key, value in group.items():
            bucket[value].append(key)
        for idx in range(len(bucket)-1, -1, -1):
            for idx2 in bucket[idx]:
                result.append(idx2)
                k -= 1
                if k == 0:
                    return result

