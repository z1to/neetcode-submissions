from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxFreq, res  = 0, 0, 0
        md = defaultdict(int)
        for r in range(len(s)):
            md[s[r]] += 1
            maxFreq = max(maxFreq, md[s[r]])
            while r - l + 1 - maxFreq > k:
                md[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


