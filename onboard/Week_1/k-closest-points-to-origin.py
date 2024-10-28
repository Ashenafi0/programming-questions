
class Solution(object):
    def kClosest(self, points, k):
        distances = []
        for point in points:
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            distances.append((distance, point))
        
        distances.sort(key=lambda x: x[0])  
        
        return [point for _, point in distances[:k]]
