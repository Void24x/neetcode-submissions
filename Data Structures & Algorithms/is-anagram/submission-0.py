class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        s_dict = {i : 0 for i in s}
        t_dict = {i:0 for i in t}

        for i in s:
            s_dict[i] = s_dict[i]+1
        for i in t:
            t_dict[i] = t_dict[i]+1
        
        if (s_dict == t_dict):
            return True
        return False
