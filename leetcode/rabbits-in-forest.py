class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic=defaultdict(int)

        for i in range(len(answers)):
            if dic[answers[i]]>0:
                dic[answers[i]]-=1
            else:
                dic[answers[i]]+=answers[i]
        no_rabbits=0
        for key,values in dic.items():
            no_rabbits+=values
        no_rabbits+=len(answers)
        return no_rabbits

        