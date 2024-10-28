class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort(reverse=True)  # Sort the piles in descending order
        n = len(piles) // 3  # Calculate the number of rounds you will play
        coins = 0
        
        for i in range(n):
            coins += piles[2 * i + 1]  
        
        return coins