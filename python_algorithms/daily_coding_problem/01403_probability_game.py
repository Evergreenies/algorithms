"""
Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two
simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number
of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the
two games and calculate their expected value.
"""

import random


def game_one() -> int:
    rolls = 0
    while True:
        roll1 = random.randint(1, 6)
        rolls += 1
        if roll1 == 5:
            roll2 = random.randint(1, 6)
            rolls += 1
            if roll2 == 6:
                return rolls


def game_two() -> int:
    rolls = 0
    while True:
        roll1 = random.randint(1, 6)
        rolls += 1
        if roll1 == 5:
            roll2 = random.randint(1, 6)
            rolls += 1
            if roll2 == 5:
                return rolls


def simulatiion(trials: int = 100) -> tuple[float, float]:
    game_one_rolls, game_two_rolls = 0, 0

    for _ in range(trials):
        game_one_rolls += game_one()
        game_two_rolls += game_two()

    return game_one_rolls / trials, game_two_rolls / trials


# Run the simulation
avg_rolls_game_one, avg_rolls_game_two = simulatiion(10000)
print(f"Expected rolls for Game 1 (5 followed by 6): {avg_rolls_game_one}")
print(f"Expected rolls for Game 2 (5 followed by 5): {avg_rolls_game_two}")

if avg_rolls_game_one < avg_rolls_game_two:
    print("Alice should choose Game 1 for a lower expected cost.")
elif avg_rolls_game_one > avg_rolls_game_two:
    print("Alice should choose Game 2 for a lower expected cost.")
else:
    print("Both games have the same expected cost.")
