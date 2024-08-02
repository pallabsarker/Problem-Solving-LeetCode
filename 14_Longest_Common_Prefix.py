class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1: return strs[0]

        prefix = strs[0]
        preLen = len(prefix)
        for st in strs[1:]:
            while prefix != st[0:preLen]:
                prefix = prefix[0:preLen - 1]
                preLen -= 1
                if preLen == 0: return ""
        return prefix
