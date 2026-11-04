from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            # Sort the characters of the string to use as a key
            sortedS = "".join(sorted(s))
            # Append the original string to its anagram group
            res[sortedS].append(s)
        
        return list(res.values())