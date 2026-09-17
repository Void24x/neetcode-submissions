class Solution:
    def findMin(self, nums: List[int]) -> int:
        max_val = max(nums)
        if( nums[-1] == max_val):
            return nums[0]

        return nums[nums.index(max_val)+1]