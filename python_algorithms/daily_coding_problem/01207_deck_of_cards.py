"""
Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, 
write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""

from random import randrange

def shuffle_deck(deck: list[int]) -> list[int]:
    length = len(deck)
    for index in range(length):
        index_j = randrange(index, length)
        deck[index], deck[index_j] = deck[index_j], deck[index]

    return deck

print(shuffle_deck([1,2,3,4,5]))
