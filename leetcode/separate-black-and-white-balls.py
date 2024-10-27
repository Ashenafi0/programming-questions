class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        white_count = 0
        black_count = 0
        result = 0

        for i in range(n):
            if s[i] == '0':
                black_count += 1
            else:
                white_count += 1

        for i in range(n):
            if s[i] == '0':
                black_count -= 1
            else:
                result += black_count

        return result

        
        