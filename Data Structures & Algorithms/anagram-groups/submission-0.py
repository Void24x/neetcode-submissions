class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for word in strs:
            k = ''.join(sorted(word))

            if k not in dic:
                dic[k] = []
            dic[k].append(word)

        return list(dic.values())
        