class Solution:
    def flipgame(self, fronts, backs):
        same = {x for x, y in zip(fronts, backs) if x == y}
        return min([x for x in fronts + backs if x not in same] or [0])