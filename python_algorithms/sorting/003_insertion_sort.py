"""
## Insertion Sort Problem Statement:
Imagine you have a deck of playing cards face down, and you want to sort 
them in **ascending order by suit (e.g., hearts, diamonds, clubs, spades)**, 
followed by **ascending order by rank (e.g., ace, 2, 3, 4, ...).**

Here's how you can achieve this using **insertion sort**:
1. **Start with the second card in the deck (index 1).**
2. **Consider it as the "current card" and the cards before it as the 
"sorted sub-array".**
3. **Compare the current card with each card in the sorted sub-array, 
starting from the end (right to left).**
4. **If the current card is **smaller** than a card in the sub-array, 
**shift that card one position to the right** to make space.**
5. **Repeat step 4 until you find a card **greater than** or equal to 
the current card, or you reach the beginning of the sub-array.**
6. **Insert the current card at the **position where shifting stopped** 
(after the larger card or at the beginning).**
7. **Repeat steps 2-6 for all remaining cards in the deck.**

This process ensures that each newly inserted card goes into its **correct 
position** within the already sorted sub-array, ultimately resulting in a 
fully sorted deck.
"""


def insertion_sort(arr: list[int]) -> list[int]:
    if not arr:
        return []

    for index in range(1, len(arr)):
        current_element = arr[index]
        prev_index = index - 1

        while prev_index >= 0 and current_element < arr[prev_index]:
            arr[prev_index + 1] = arr[prev_index]
            prev_index -= 1

        arr[prev_index + 1] = current_element

    return arr


if __name__ == "__main__":
    assert insertion_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
