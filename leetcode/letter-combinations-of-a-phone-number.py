class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        ans=[]
        def bc(comb,index):
            if  len(comb)==len(digits):
                ans.append(comb)
                return
            
            for i in range(index,len(digits)):
                for j in range(len(dic[digits[i]])):
                    bc(comb + dic[digits[i]][j],i+1)
                    
        bc("",0)
        return [] if ans[0]=="" else ans


        