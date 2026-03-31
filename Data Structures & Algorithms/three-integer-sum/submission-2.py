class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    
                    # skip duplicates l
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # skip duplicates r  
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
        return result