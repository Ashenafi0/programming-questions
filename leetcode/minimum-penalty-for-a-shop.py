class Solution:
    def bestClosingTime(self, customers: str) -> int:
        no_y=customers.count("Y")
        no_n=customers.count("N")

        num_n=0
        output=0
        penality=[]
        for i in range(len(customers)):
            penality.append(no_y+num_n)
            if customers[i]=="Y":
                no_y-=1
            else:
                num_n+=1
        penality.append(no_n)
        output=min(penality)
        for i in range(len(penality)):
            if penality[i]==output:
                return i

            





    

        