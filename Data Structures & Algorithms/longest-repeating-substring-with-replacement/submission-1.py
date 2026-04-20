from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxFreq, res = 0, 0, 0
        cd = defaultdict(int)
        for r in range(len(s)):
            cd[s[r]] += 1
            maxFreq = max(maxFreq, cd[s[r]])
            while r - l + 1 - maxFreq > k: # while is invalid
                cd[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
