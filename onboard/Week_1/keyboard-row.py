class Solution(object):
    def findWords(self, words):
        row_1={"Q","W","E","R","T","Y","U","I","O","P"}
        row_2={"A","S","D","F","G","H","J","K","L"}
        row_3={"Z","X","C","V","B","N","M"}
        ans=[]
        for i in range(len(words)):
            if set(words[i].upper()).issubset(row_1):
                ans.append(words[i])
            elif set(words[i].upper()).issubset(row_2):
                ans.append(words[i])
            elif set(words[i].upper()).issubset(row_3):
                ans.append(words[i])
        return ans


            

        