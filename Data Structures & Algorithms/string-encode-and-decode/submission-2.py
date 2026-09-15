class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for e in strs:
            enc = enc+str(len(e))+'_'+e
        return enc         
    def decode(self, s: str) -> List[str]:
        ans = []

        i = 0

        while(i < len(s)):
            j = i

            while(s[j] != '_'):
                j += 1
            
            l = int(s[i:j])

            w = s[j+1: j+1+l]

            ans.append(w)

            i = j + 1 + l

        return ans

        
