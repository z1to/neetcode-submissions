class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nmap = {}
        for n in nums:
            nmap[n] = 0
        
        for n in nums:
            if n in nmap:
                nmap[n] = nmap[n] + 1
            if nmap[n] > 1:
                return True
        
        return False