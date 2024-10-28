class Solution(object):
    def totalMoney(self, n):
        weeks = n // 7
        days = n % 7
        total = 0
        for i in range(weeks):
            total += 28 + 7 * i
        for i in range(1, days + 1):
            total += weeks + i
        return total