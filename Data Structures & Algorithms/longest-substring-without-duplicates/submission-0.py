class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        ans  = 0
        chars = set()
        ## keep track of the dup chars in the current substring window
        while(r < len(s)):
            ##if not present add it to the list of seen chars in the current substring
            if s[r] not in chars:
                chars.add(s[r])
                ans = max(ans,r-l+1)
                r += 1
            ##if present, shrink the window from left untill the chr is removed from the seen char's list  
            else:
                chars.remove(s[l])
                l +=1
        return ans
            

        