class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()

        trainers.sort()
        p1=0
        p2=0
        match=0
        while p1 <len(trainers) and p2<len(players):
            while p1<len(trainers) and  players[p2]>trainers[p1] :
                p1+=1
            if p1>= len(trainers):
                return match
            match+=1
            p2+=1
            p1+=1
        return match
        