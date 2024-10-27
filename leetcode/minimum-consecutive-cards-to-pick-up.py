class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic={}
        ans=float("inf")
        
        for i in range(len(cards)):
            if cards[i] in dic:
                ans=min(ans, i-dic[cards[i]]+1)
            dic[cards[i]]=i
        return -1 if ans==float("inf") else ans
        