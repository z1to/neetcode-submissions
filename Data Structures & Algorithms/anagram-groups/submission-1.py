from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs: 
            sortstr = ''.join(sorted(s))
            # print(sortstr)
            if sortstr not in d:
                d[sortstr] = []
            d[sortstr].append(s)
        return list(d.values())