class Solution:
    def isHappy(self, n: int) -> bool:
        def squares(n):
            sum = 0
            while n > 0:
                rem = n % 10
                sum = sum + rem**2
                n = n // 10
            return sum

        check_list = []
        while True:
            n = squares(n)
            if n == 1: return True
            if n not in check_list:
                check_list.append(n)
            else: return False

