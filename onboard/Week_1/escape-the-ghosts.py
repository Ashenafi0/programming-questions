class Solution(object):
    def escapeGhosts(self, ghosts, target):
        distance_destination=abs(target[0])+abs(target[1])
        for x,y in ghosts:
            catch_distance=abs(x-target[0])+abs(y-target[1])
            if catch_distance<=distance_destination:
                return False
        return True

        