class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix_sum=[0]*n

        for i in range(len(bookings)):
            start,end,seat=bookings[i]
            prefix_sum[start-1]+=seat
            if end<len(prefix_sum):
                prefix_sum[end]+=-seat
        accumulator=0
        ans=[]
        for i in range(n):
            accumulator+=prefix_sum[i]
            ans.append(accumulator)
        return ans
            
            


        