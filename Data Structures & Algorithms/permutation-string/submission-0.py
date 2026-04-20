from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, ls1 = 0, len(s1)
        s1c = defaultdict(int)
        for s in s1:
            s1c[s] += 1
        wc = defaultdict(int)
        for r in range(len(s2)):
            wc[s2[r]] += 1
            while r - l + 1 > ls1:
                wc[s2[l]] -= 1
                if wc[s2[l]] == 0:
                    del wc[s2[l]]
                l += 1
            if s1c == wc: 
                return True
        return False