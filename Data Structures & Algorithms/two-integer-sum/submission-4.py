class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lmap = {}
        
        for i,n in enumerate(nums):
            lmap[n] = i
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in lmap and lmap[diff] != i:
                return [i, lmap[diff]]