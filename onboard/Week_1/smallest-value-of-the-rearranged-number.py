class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return num
        sign = 1
        if num < 0:
            sign = -1
            num = abs(num)
        
        num_str = list(str(num))  
        num_str.sort(reverse=(sign == -1))
        if sign==1 and num_str[0]=="0":
            i=0
            while num_str[i]=="0" and i<len(num_str):
                i+=1
            if i<len(num_str):
                num_str[0],num_str[i]=num_str[i],num_str[0]

        
        return sign * int("".join(num_str))
