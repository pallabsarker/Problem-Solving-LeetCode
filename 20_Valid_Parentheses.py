class Solution:
    def isValid(self, s: str) -> bool:
        
        # main = True
        # while main:
        #     length = len(s)
        #     for i in ["()","{}","[]"]:
        #         s = s.replace(i,"")
        #     if length == len(s): 
        #         main = False
        # return s == "" 
        
        parentheses = {"(":")", "{":"}", "[":"]"}
        stack = []
        
        for i in s:
            if i in parentheses.keys(): stack.append(i)
            elif stack == [] or i != parentheses[stack.pop()]: return False
        return stack == []