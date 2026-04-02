class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lmap = {}
        for i, n in enumerate(nums):
            if target - n in lmap:
                return [lmap[target - n],i]
            lmap[n] = i
                



