class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        by iterating from the first start point up to the last destination add when we get the passenger to be picked up and subtract when the passenger drop off, then if there is a point where there are more passengers than the capacity of the car we retutn false else return true
        """
        zipped = list(zip(*trips))
        starting_point = min(zipped[1])
        ending_point = max(zipped[1])

        my_car = [0] * (ending_point - starting_point + 2)
        currentPassengers = 0

        for num_passengers, pickup, dropoff in  trips:
            my_car[pickup - starting_point + 1] += num_passengers
            if dropoff - starting_point <= ending_point - starting_point:
                my_car[dropoff - starting_point + 1] -= num_passengers

        for indx in range(1, ending_point - starting_point + 2):
            my_car[indx] += my_car[indx - 1]
            if my_car[indx] > capacity:
                return False

        return True