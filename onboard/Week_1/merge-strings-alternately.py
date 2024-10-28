class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l,r=0,0
        merged=[]
        while l<len(word1) and r<len(word2):
            merged.append(word1[l])
            merged.append(word2[r])
            l+=1
            r+=1
        merged.append(word1[l:])
        merged.append(word2[r:])
        return "".join(merged)

        

        

        