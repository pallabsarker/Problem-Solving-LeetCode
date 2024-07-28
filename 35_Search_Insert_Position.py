class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        while True:
            if target in nums:
                t = nums.index(target)
                break
            else:
                nums.append(target)
                nums = sorted(nums)
        return t
