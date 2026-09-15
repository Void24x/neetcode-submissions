class Solution:
    def maxArea(self, h: List[int]) -> int:
        max_vol = 0
        l = 0
        r = len(h)-1
        while(l < r):
            width = r-l
            height = min(h[l], h[r])

            cur_vol = width*height
            max_vol = max(cur_vol, max_vol)

            if(h[l] < h[r]):
                l+=1
            else:
                r-=1
        
        return max_vol

## Correct Pointer approach for O(n)
## i-->..................<--j

        