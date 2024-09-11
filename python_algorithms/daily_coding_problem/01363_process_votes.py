"""
On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file.
Write a program that reads this file as a stream and returns the top 3 candidates at any given time.
If you find a voter voting more than once, report this as fraud.
"""

import heapq
from collections import defaultdict


def process_votes(stream: list) -> None:
    vote_count = defaultdict(int)
    voters = set()
    top_candidates = []

    for voter_id, candidate_id in stream:
        if voter_id in voters:
            print(f"Froud detected: Voter {voter_id} has voted more than once!")
            continue

        voters.add(voter_id)
        vote_count[candidate_id] += 1
        heapq.heappush(top_candidates, (vote_count[candidate_id], candidate_id))

        if len(top_candidates) > 3:
            heapq.heappop(top_candidates)

        print(f"Current top 3 candiates: {sorted(top_candidates, reverse=True)}")


stream = [
    (1, "A"),
    (2, "B"),
    (3, "A"),
    (4, "C"),
    (5, "B"),
    (6, "A"),
    (1, "C"),  # Fraud case
    (7, "C"),
    (8, "A"),
    (9, "B"),
]
process_votes(stream)
