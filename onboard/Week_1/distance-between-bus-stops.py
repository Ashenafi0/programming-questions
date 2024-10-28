class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        if start == destination:
            return 0
        
        total_distance = sum(distance)
        clockwise_distance = 0
        cur_stop = start
        
        while cur_stop != destination:
            clockwise_distance += distance[cur_stop]
            cur_stop = (cur_stop + 1) % len(distance)
        
        return min(clockwise_distance, total_distance - clockwise_distance)

        