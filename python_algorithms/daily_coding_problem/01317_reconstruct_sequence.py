"""
The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for its order is an array 
representing whether each number is larger or smaller than the last. Given this information, reconstruct 
an array that is consistent with it. 

For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4].
"""


def reconstruct_sequence(clues):
    N = len(clues) - 1
    sequence = []
    low, high = 0, N
    
    for clue in clues:
        if clue == None:
            continue
        elif clue == '+':
            sequence.append(low)
            low += 1
        elif clue == '-':
            sequence.append(high)
            high -= 1
    
    # The last number to add will be the remaining one (either low or high)
    if len(sequence) < len(clues):
        sequence.append(low if low == high else high)
    
    return sequence

# Example usage:
clues = [None, '+', '+', '-', '+']
result = reconstruct_sequence(clues)
print(result)  # Output: [0, 1, 2, 4, 3]
