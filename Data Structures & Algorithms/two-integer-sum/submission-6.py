class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       lmap = {}

       for i, num in enumerate(nums):
            if target - num in lmap:
                return [lmap[target - num], i]
            lmap[num] = i
                



