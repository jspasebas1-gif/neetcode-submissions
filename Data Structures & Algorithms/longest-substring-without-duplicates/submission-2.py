class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        seen = set()
        res = 1
        
        l, r = 0, 1
        seen.add(s[l])

        while r < len(s):
            if s[r] in seen:
                
                while s[l] != s[r]:               
                    seen.remove(s[l])
                    
                    l+=1
                seen.remove(s[l])
                l+=1
                seen.add(s[r])
                r+=1
                res = max(res, len(seen))
            else:
                seen.add(s[r])
                r+=1
                res = max(res,len(seen))
        return res
                
               
              
            

        