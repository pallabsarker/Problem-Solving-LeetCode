class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        new_n = (bin(n)[2:])
        for i in range(len(new_n)):
            if "1" in new_n[i]:
                c += 1
        return c
