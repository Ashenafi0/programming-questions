class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target_count = n // 4
        excess_counts = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        
        for char in s:
            excess_counts[char] += 1
        
        excess = {char: max(0, excess_counts[char] - target_count) for char in excess_counts}
        
        if all(count == 0 for count in excess.values()):
            return 0
        
        min_length = float('inf')
        left = 0
        
        for right, char in enumerate(s):
            excess[char] -= 1
            
            while all(count <= 0 for count in excess.values()):
                min_length = min(min_length, right - left + 1)
                excess[s[left]] += 1
                left += 1
        
        return min_length
