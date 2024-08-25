List = list
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2 = set()
        for i in nums:
            if i in nums2: return True
            nums2.add(i)
        return False
print(Solution().containsDuplicate([1,2,3,1]))
print(Solution().containsDuplicate([1,2,3,4]))
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))