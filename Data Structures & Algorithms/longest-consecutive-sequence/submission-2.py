class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int) # handles missing key, avoids missing key errors, will create the key if not present. 
        ls = 0 # longest streak
        
        for n in nums:
            if not mp[n]:  # Is mp[n] non-zero? No, it's 0 (default). The condition is TRUE. (did we process this number already?)
                mp[n] = mp[n - 1] + mp[n + 1] + 1  # length of mp[n] = len(left boundary) + len(right boundary) + 1
                mp[n - mp[n - 1]] = mp[n] # mp[n - left] = len(mp[n]) -> (Updating left boundary)
                mp[n + mp[n + 1]] = mp[n] # mp[n + right] = len(mp[n]) -> (Updating right boundary)
                ls = max(ls, mp[n]) # compare ls to mp[n] whichever is larger, set to ls
        return ls        

"""
Think of mp[x] not just as "the length associated with x", 
but more specifically as: 
"If x is the endpoint (either minimum or maximum) of a known consecutive sequence,
mp[x] stores the total length of that sequence." 
"""