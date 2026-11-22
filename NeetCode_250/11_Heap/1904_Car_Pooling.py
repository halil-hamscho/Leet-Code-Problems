"""

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Passengers are dropped off before new passengers are picked up at the same location. At every point along the route, the total number of passengers in the car must not exceed capacity.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.


"""
import heapq

class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:

        trips.sort(
            key=lambda trip: trip[1]
        ) # we sort by we from key

        # Each entry to the min heap is added capacity
        min_heap = []
        # (end_location, num_passengers)
        curr_capacity = 0
        for passengers, start, end in trips:

            # Remove passengers whose destinations we have reached
            while min_heap and min_heap[0][0] <= start:
                _, c = heapq.heappop(min_heap)
                curr_capacity -= c

            # Add if we have capacity
            if passengers + curr_capacity > capacity:
                return False

            heapq.heappush(min_heap, (end, passengers))
            curr_capacity += passengers

        return True

if __name__ == "__main__":
    trips = [[2,1,5],[3,5,7]]
    capacity = 3
    sol = Solution()
    result = sol.carPooling(trips, capacity)