class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sorted_trips = sorted(trips, key=lambda x: x[-1])
        prefix_sum=[0]*sorted_trips[-1][-1]

        for i in range(len(trips)):
            no_pass,start,end=trips[i]
            prefix_sum[start]+=no_pass
            if end<len(prefix_sum):
                prefix_sum[end]+=-no_pass
            accumulator=0
        for i in range(len(prefix_sum)):
            accumulator+=prefix_sum[i]
            prefix_sum[i]=accumulator
            if prefix_sum[i]>capacity:
                return False
        return True
        


       
    

        