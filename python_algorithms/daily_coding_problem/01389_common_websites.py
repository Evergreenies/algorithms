"""
You are given a list of (website, user) pairs that represent users
visiting websites. Come up with a program that identifies the top
k pairs of websites with the greatest similarity.

For example, suppose k = 1, and the list of tuples is:

[('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5)
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e': 5), ('e', 6)]

Then a reasonable similarity metric would most likely conclude that
a and e are the most similar, so your program should return
[('a', 'e')].
"""

from collections import defaultdict
from itertools import combinations


def similar_websites(pairs: list, k: int) -> list | None:
    website_users = defaultdict(set)
    for webiste, user in pairs:
        website_users[webiste].add(user)

    similarity_score = []
    for (website1, user1), (website2, user2) in combinations(website_users.items(), 2):
        intersection_size = len(user1 & user2)
        union_size = len(user1 | user2)

        jaccard_similarity = intersection_size / union_size if union_size > 0 else 0
        similarity_score.append(((website1, website2), jaccard_similarity))

    similarity_score.sort(key=lambda x: x[1], reverse=True)
    top_k_pairs = [pair for pair, _ in similarity_score[:k]]

    return top_k_pairs


pairs = [
    ("a", 1),
    ("a", 3),
    ("a", 5),
    ("b", 2),
    ("b", 6),
    ("c", 1),
    ("c", 2),
    ("c", 3),
    ("c", 4),
    ("c", 5),
    ("d", 4),
    ("d", 5),
    ("d", 6),
    ("d", 7),
    ("e", 1),
    ("e", 3),
    ("e", 5),
    ("e", 6),
]
k = 1
print(similar_websites(pairs, k))
