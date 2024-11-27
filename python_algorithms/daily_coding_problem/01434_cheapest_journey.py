"""
You are given a huge list of airline ticket prices between different cities around the world
on a given day. These are all direct flights. Each element in the list has the format
(source_city, destination, price).

Consider a user who is willing to take up to k connections from their origin city A to their
destination B. Find the cheapest fare possible for this journey and print the itinerary for
that journey.

For example, our traveler wants to go from JFK to LAX with up to 3 connections, and our input
flights are as follows:

[
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]
Due to some improbably low flight prices, the cheapest itinerary would be
JFK -> ATL -> ORD -> LAX, costing $440.
"""

from collections import defaultdict, deque


def find_cheapest_fare_no_heapq(flights, start, destination, k):
    # Build adjacency list
    graph = defaultdict(list)
    for src, dest, price in flights:
        graph[src].append((dest, price))

    # Queue: (cost, city, stops_remaining, path)
    queue = deque([(0, start, k + 1, [start])])  # Initialize queue with the start city

    min_cost = float("inf")
    best_path = None

    while queue:
        cost, city, stops, path = queue.popleft()

        # If destination is reached, check if the cost is the minimum
        if city == destination:
            if cost < min_cost:
                min_cost = cost
                best_path = path
            continue

        # If stops remain, explore the next cities
        if stops > 0:
            for neighbor, price in graph[city]:
                new_cost = cost + price
                # Only continue if the new cost is less than the current minimum cost
                if new_cost < min_cost:
                    queue.append((new_cost, neighbor, stops - 1, path + [neighbor]))

    return (min_cost, best_path) if best_path else None


# Example Usage
flights = [
    ("JFK", "ATL", 150),
    ("ATL", "SFO", 400),
    ("ORD", "LAX", 200),
    ("LAX", "DFW", 80),
    ("JFK", "HKG", 800),
    ("ATL", "ORD", 90),
    ("JFK", "LAX", 500),
]

start = "JFK"
destination = "LAX"
k = 3

result = find_cheapest_fare_no_heapq(flights, start, destination, k)
if result:
    cost, path = result
    print(f"Cheapest fare: ${cost}")
    print(f"Itinerary: {' -> '.join(path)}")
else:
    print("No valid itinerary found.")
