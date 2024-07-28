class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits) - 1 
        while l >= 0:
            if digits[l] + 1 == 10:
                digits[l] = 0
                if l == 0 and digits[l] == 0:
                    digits.insert(0, 1)
            else: 
                digits[l] += 1
                break
            l -= 1
        return digits
