class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodl =  []
        for n in nums:
            temp = nums.copy()
            temp.remove(n)
            prod = 1
            for num in temp:
                prod *= num
            prodl.append(prod)
        return prodl






# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]
