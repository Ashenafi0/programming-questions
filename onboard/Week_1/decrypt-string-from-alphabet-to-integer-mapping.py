class Solution(object):
    def freqAlphabets(self, s):
        result = ''
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                letter = chr(int(s[i:i + 2]) + ord('a') - 1)
                result += letter
                i += 3
            else:
                letter = chr(int(s[i]) + ord('a') - 1)
                result += letter
                i += 1
        return result
