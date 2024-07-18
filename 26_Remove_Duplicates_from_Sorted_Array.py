class Solution:
    def removeDuplicates(self, nums: List[int]) -> list:
        c = 0
        for i in range(len(nums)):
            if(i < len(nums) - 1 and nums[i] == nums[i + 1]): continue
            else: 
                nums[c] = nums[i]
                c += 1
        return c



        
