"""
**Challenge:**
Calculating reliable statistics sometimes involves **excluding outliers**, which are 
extreme values that can significantly skew the overall results. This algorithm helps 
you achieve this by **trimming** a given dataset (array).

**Context:**
* This approach is often used to calculate **robust** statistics, such as the 
**trimmed mean**, which is less sensitive to outliers compared to the standard mean.
* It is particularly applicable in scenarios like calculating an **athlete's average 
score**, where exceptional performances or low scores might not accurately represent 
their typical performance.

**Functionality:**
* The algorithm takes an array of values (dataset) and a **percentage** to be 
neglected as input.
* It **sorts** the array to efficiently identify outliers.
* Based on the provided percentage, the algorithm **excludes** a specific portion of 
elements from both ends of the sorted array:
    * The specified percentage (e.g., 20%) represents the **combined** portion to be 
    excluded, meaning both the top and bottom portions will contribute equally.
    * For a 20% exclusion, the top 10% and the bottom 10% of the sorted array would be 
    disregarded.
* The remaining elements (after excluding the specified portions) are used to calculate 
the **trimmed mean** (or any other desired statistic).

**Key Points:**
* This algorithm focuses on **trimming** a dataset, not directly calculating statistics 
like the mean.
* The time complexity of this algorithm is O(n), meaning its execution time grows linearly 
with the size of the input array (due to sorting).
"""


def trim_dataset(arr: list[int], percentage: int) -> list[int]:
    if not arr:
        return []

    if percentage < 0 or percentage > 100:
        raise ValueError("percentage must be between 0 and 100")

    arr.sort()
    to_ignore = int(len(arr) * percentage / 100)
    return arr[to_ignore:-to_ignore]


if __name__ == "__main__":
    assert trim_dataset([10, 5, 20, 15, 8, 25], 20) == [8, 10, 15, 20]
