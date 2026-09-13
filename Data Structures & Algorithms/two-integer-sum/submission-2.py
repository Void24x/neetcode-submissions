class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # l = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i]+nums[j] == target):
        #             l.append(i)
        #             l.append(j)
        #             return l  
        seen = {}
        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in seen:
                return [seen[comp], i]

            seen[nums[i]] = i     