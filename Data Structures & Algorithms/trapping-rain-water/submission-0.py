class Solution:
    def trap(self, h: List[int]) -> int:
        l = 0
        r = len(h)-1

        l_max = 0
        r_max = 0

        water = 0

        while (l<r):

            if( h[l] <= h[r]):

                if(l_max <= h[l]):
                    l_max = h[l]
                else:
                    water = water + (l_max-h[l])

                l+=1
            else:

                if(r_max <= h[r]):
                    r_max = h[r]
                else:
                    water += r_max-h[r]
                r -=1

        return water




#For every position, the water above it is determined by the shorter of the tallest bar on its left and the tallest bar on its right

        