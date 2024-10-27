class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        orginal=list(p)
        orginal.sort()
        temp=[]
        ans=[]
        l=0
        for r in range(len(s)):
            temp.append(s[r])
            if r-l+1==len(orginal):
                if orginal==sorted(temp):
                    ans.append(l)
                temp=temp[1:]
                l+=1
        return ans




       



        