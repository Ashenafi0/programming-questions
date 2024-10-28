class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        def check(input1,input2):
            i=0
            ans=""
            while i< len(input1) and i<len(input2):
                if input1[i]==input2[i]:
                    ans+=input1[i]
                else:
                    break
                i+=1
            return ans
        ans=strs[0]
        for i in range(1,len(strs)):
            ans=check(ans,strs[i])
        return ans

                

        