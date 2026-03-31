class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        lcs = 0

        for n in nums:
            k, streak = n, 0
            while k in ns: 
                streak += 1
                k += 1
            
            if streak > lcs:
                lcs = streak
        
        return lcs
