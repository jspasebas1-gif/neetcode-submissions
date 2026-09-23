class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        result = []
        for char in strs:
            key = tuple(sorted(char))
            if key not in groups:
                groups[key] = []
                groups[key].append(char)
            else:
                groups[key].append(char)
        return list(groups.values())

        