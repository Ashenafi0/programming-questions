class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel={"a","e","i","o","u"}

        l=0
        count=0
        no_vowel=0
        for r in range(len(s)):
            if s[r] in vowel:
                no_vowel +=1
            if r-l+1==k:
                count=max(count,no_vowel)
                if s[l] in vowel:
                    no_vowel-=1
                l+=1
        return count

        