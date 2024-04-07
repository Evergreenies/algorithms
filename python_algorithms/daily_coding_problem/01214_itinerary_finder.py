"""

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, 
and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If 
there are multiple possible itineraries, return the lexicographically smallest one. All flights must 
be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] 
and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you 
should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid 
itinerary. However, the first one is lexicographically smaller.

"""

from collections import defaultdict
from functools import wraps


def find_itinerary(flights: list[tuple[str, str]], start: str) -> list[str] | None:
    destinations = defaultdict(list)
    for origin, destination in flights:
        destinations[origin].append(destination)

    def explore(current: str, visited: set, itinerary: list) -> list[str] | None:
        itinerary.append(current)
        if len(itinerary) == len(flights) + 1:
            return itinerary

        for _next_desti in sorted(destinations[current]):
            if _next_desti not in visited:
                visited.add(_next_desti)
                result = explore(_next_desti, visited.copy(), itinerary.copy())

                if result:
                    return result

                visited.remove(_next_desti)

        itinerary.pop()
        return None

    visited = set([start])
    itinerary = []
    result = explore(start, visited, itinerary)
    return result if result else None


if __name__ == "__main__":
    flights = [("SFO", "HKO"), ("YYZ", "SFO"), ("YUL", "YYZ"), ("HKO", "ORD")]
    start = "YUL"
    itinerary = find_itinerary(flights, start)
    print(itinerary)  # Output: ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

    flights = [("SFO", "COM"), ("COM", "YYZ")]
    start = "COM"
    itinerary = find_itinerary(flights, start)
    print(itinerary)  # Output: None

    flights = [("A", "B"), ("A", "C"), ("B", "C"), ("C", "A")]
    start = "A"
    itinerary = find_itinerary(flights, start)
    print(itinerary)
