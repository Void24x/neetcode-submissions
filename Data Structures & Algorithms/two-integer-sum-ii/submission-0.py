class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1
        ans_i =[]
        while(i < j):
            sum = nums[i]+nums[j]
            if (sum == target):
                ans_i.append(i+1)
                ans_i.append(j+1)

                return ans_i
            elif (sum > target):
                if(nums[i] > nums[j]):
                    i+=1
                else:
                    j-=1
            else:
                if(nums[i] > nums[j]):
                    j-=1
                else:
                    i+=1
            
        