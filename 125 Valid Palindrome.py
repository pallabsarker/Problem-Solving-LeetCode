class Solution:
    def isPalindrome(self, s: str) -> bool:

        us = ""
        for i in range(len(s)):
            if s[i].isalnum():
                us += s[i].lower()

        l = len(us)
        if l % 2 != 0:
            c = l // 2
            us = us[:c] + us[c + 1:]
            l = len(us)
    
        us1 = us[:l // 2]
        us2 = us[l // 2:][::-1]
        return us1 == us2

        # n = len(s)
        # left = 0
        # right = n - 1

        # while left < right:
        #     if not s[left].isalnum():
        #         left += 1
        #         continue
    
        #     if not s[right].isalnum():
        #         right -= 1
        #         continue
    
        #     if s[left].lower() != s[right].lower(): return False
    
        #     left += 1
        #     right -= 1

        # return True
