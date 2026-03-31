class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ls = 0

        for n in nums:
            k = n
            streak = 1
            while k + 1 in nums:
                streak += 1
                k += 1
            ls = max(ls, streak)
        return ls
