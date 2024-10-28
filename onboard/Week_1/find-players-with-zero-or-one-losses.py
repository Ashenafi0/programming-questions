class Solution(object):
    def findWinners(self, matches):
        losses = {}
        
        for winner, loser in matches:
            losses[loser] = losses.get(loser, 0) + 1
            
            if winner not in losses:
                losses[winner] = 0
        
        no_losses = [player for player, num_losses in losses.items() if num_losses == 0]
        one_loss = [player for player, num_losses in losses.items() if num_losses == 1]
        
        no_losses.sort()
        one_loss.sort()
        
        return [no_losses, one_loss]
