"""
## Selection Sort Problem Statement:
Imagine you have a messy bookshelf with books scattered in no particular order. 
You want to **arrange them alphabetically** (ascending order) but can only **move 
one book at a time**. 

Here's how you approach it:
1. **Start at the beginning of the shelf (index 0).**
2. **Find the book with the **smallest title** among the remaining books 
(excluding the one you're currently at).**
3. **Swap the positions of the book you're currently at with the book having 
the smallest title.**
4. **Repeat steps 2 and 3 for the remaining books on the shelf.**
"""


def selection_sort(arr: list[int]) -> list[int]:
    length = len(arr)
    for index_i in range(length):
        min_index = index_i
        for index_j in range(index_i + 1, length):
            if arr[index_j] < arr[min_index]:
                min_index = index_j

        arr[index_i], arr[min_index] = arr[min_index], arr[index_i]

    return arr


if __name__ == "__main__":
    assert selection_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
