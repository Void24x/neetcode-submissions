class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        md = {item: 0 for item in nums }
        for i in nums:
            md[i] = md[i]+1
        flag = 0
        for value in md.values():
            if value > 1:
                flag = 1
                break;
        if flag == 1:
            return True
        else:
            return False;

        