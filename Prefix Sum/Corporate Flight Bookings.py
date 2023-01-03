from itertools import accumulate
class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        answer = [0]*n
        for booking in bookings:
            answer[booking[0] - 1] += booking[2]
            if booking[1] < n:
                answer[booking[1]] -= booking[2]
        
        answer = list(accumulate(answer))
        
        return answer