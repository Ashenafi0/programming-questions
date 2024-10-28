class Solution(object):
    def wateringPlants(self, plants, capacity):
        steps = 0
        current_water = 0
        n = len(plants)
        for i in range(n):
            if plants[i] > capacity:
                return -1  

            if plants[i] > current_water:
                steps += (i * 2)  
                current_water = capacity

            current_water -= plants[i]

        return steps + n  
