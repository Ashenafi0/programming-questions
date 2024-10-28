class Solution(object):
    def restoreString(self, s, indices):
        split_char=[""]*len(s)
        for i in range(len(s)):
            split_char[indices[i]]=s[i]
        return "".join(split_char)
       