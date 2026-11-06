class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        res = 0

        for r in range(len(s)):
            if s[r] in seen:
                new = r - l
                res = max(res, new)
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
                seen.add(s[r])
                r+=1
            else:
                seen.add(s[r])
                r+=1
                new = r - l
                res = max(res, new)
        return res

        