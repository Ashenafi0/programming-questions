class Solution(object):
    def interpret(self, command):
        i=0
        res=""
        while i<len(command):
            if command[i]=="G":
                res+="G"
                i+=1
            else:
                if command[i:i+2]=="()" :
                    res+="o"
                    i+=2
                else:
                    res+="al"
                    i+=4
            
        return res


       
        