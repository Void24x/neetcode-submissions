class Solution:
    def calcTotalTimeTofinishPile(self,piles: List[int], perHour: int) -> int:
            t = 0
            for e in piles:
                t += math.ceil(e/perHour)
            return t
            
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        ans = 0
        
        while(l<=r):
            mid = (l+r)//2
            k = self.calcTotalTimeTofinishPile(piles, mid)
            if(k<=h):
                ans = mid
                r = mid-1
            else:
                l = mid +1
        return ans

    
        