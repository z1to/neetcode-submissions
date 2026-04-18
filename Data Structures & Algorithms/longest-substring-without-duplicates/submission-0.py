from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        cd = defaultdict(int)
        maxl = 0
        for r in range(len(s)):
            while s[r] in cd:
                del cd[s[l]]
                l+=1
            cd[s[r]] = 1
            maxl = max(maxl, r - l +1)
        return maxl 

            
            
