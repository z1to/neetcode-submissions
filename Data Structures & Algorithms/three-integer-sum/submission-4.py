class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() # [-4, -1, -1, 0, 1, 2]
        
        # len - 2 to give room for l and r, i is fixed. 
        for i in range(len(nums) - 2):
            
            # if not first index, check the previous value for duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i+1, len(nums) - 1
           
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    
                    # keep skipping duplicate l's
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # keep skipping duplicate r's 
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                
                # if sum is negative move l to larger num
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                
                # if sum is positive move r to smaller num
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
        
        return result