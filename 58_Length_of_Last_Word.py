class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c, count = len(s)-1, 0
        while True:
            if s[c] == " ": c -= 1
            else: break
        while True:
            if s[c] != " " and c >= 0: 
                c -= 1
                count += 1
            else: break
        return count
