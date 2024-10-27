class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic={5:0,10:0,20:0}

        for i in range(len(bills)):
            if bills[i]==5:
                dic[5]+=1
            elif bills[i]==10:
                if dic[5]>0:
                    dic[5]-=1
                    dic[10]+=1
                else:
                    return False
            else:
                if dic[5]>0 :
                    if dic[10]==0 and dic[5]<3:
                        return False
                    elif dic[10]==0 and dic[5]>=3:
                        dic[5]-=3
                        dic[20]+=1
                    elif dic[10]>0:
                        dic[5]-=1
                        dic[10]-=1
                        dic[20]+=1


                    
                    
                else:
                    return False
        return True

                

        