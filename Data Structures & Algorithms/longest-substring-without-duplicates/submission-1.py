from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxl = 0, 0
        dd = defaultdict(int)
        for r in range(len(s)):
            while s[r] in dd:
                del dd[s[l]]
                l += 1
            dd[s[r]] += 1
            maxl = max(maxl, r - l +1)
        return maxl
            
            
