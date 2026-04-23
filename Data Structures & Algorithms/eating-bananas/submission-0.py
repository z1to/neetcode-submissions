from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        # isValid = sum(ceil(piles[i] / k)) <= h
        # [1,4,3,2], h = 9
        # 1/2 =0.5 ->1, 4/2=2
        minr = max(piles)
        while l <= r: 
            mid = (l + r) // 2
            k = sum(ceil(p / mid) for p in piles)
            if k <= h:
                minr = min(minr, mid)
                r = mid - 1 
            else:
                l = mid + 1
        return minr
