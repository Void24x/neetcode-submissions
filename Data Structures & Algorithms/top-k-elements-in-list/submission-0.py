class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for e in nums:
            if e not in dic.keys():
                dic[e] = 1
            else:
                dic[e] = dic[e]+1
        ans = list(dict(sorted(dic.items(), key=lambda x:x[1], reverse=True)).keys())
        ans_f = []
        for i in range(0, k):
            ans_f.append(ans[i])
        return ans_f

        