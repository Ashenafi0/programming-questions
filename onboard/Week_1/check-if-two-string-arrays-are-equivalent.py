class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        input1=""
        input2=""
        for arr in word1:
            input1+=arr
        for arr in word2:
            input2+=arr
        return input1==input2
        
       
        