class Solution(object):
    def numberOfMatches(self, n):
        res = 0
        while n != 1:
            if n % 2 == 0:
                res += n // 2
                n //= 2
            else:
                res += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return res
