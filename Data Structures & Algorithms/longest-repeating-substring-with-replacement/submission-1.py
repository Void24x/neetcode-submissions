from collections import defaultdict 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        maxf = 0
        maxlen = 0
        ##O(2N) + O(26)
        freqmap = defaultdict(int)

        while r < len(s):
            freqmap[s[r]] +=1
            maxf = max(maxf, freqmap[s[r]])

            while (r-l+1) - maxf > k:
                freqmap[s[l]] -= 1
                maxf = 0
                for v in freqmap.values():
                    maxf = max(maxf, v)
                l +=1
            if (r-l+1) - maxf <= k:
                maxlen = max(maxlen, r-l+1)
            r +=1
        return maxlen
        