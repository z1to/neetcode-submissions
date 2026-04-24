from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # rate of eating
        # isValid = sum(ceil(p / k=mid)) <= h
        # [1,4,3,2], h = 9
        # 1/2 = ceil(0.5) -> 1, 4/2 = 2 -> 1
        minr = max(piles) # min rate of eating
        while l <= r: 
            mid = (l + r) // 2 # rate of eating
            k = sum(ceil(p / mid) for p in piles)
            if k <= h:
                minr = min(minr, mid)
                r = mid - 1 
            else:
                l = mid + 1
        return minr
