class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return (sorted(nums)[len(nums) // 2])

        # counts = {}
        # for i in nums:
        #     if i not in counts:
        #         counts[i] = 1
        #     else: counts[i] += 1

        #     if counts[i] > len(nums) / 2:
        #         return i
