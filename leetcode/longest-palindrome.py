class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_freq=Counter(s)

        len_palindrom=0
        flag=False

        for val in char_freq.values():
            if val%2==0:
                len_palindrom+=val
            else:
                len_palindrom+=val-1
                flag=True
        if flag:
            len_palindrom+=1
        return len_palindrom
        