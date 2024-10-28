class Solution(object):
    def isCovered(self, ranges, left, right):
        covered = set()
        for start, end in ranges:
            for i in range(start, end + 1):
                covered.add(i)

        for num in range(left, right + 1):
            if num not in covered:
                return False

        return True
