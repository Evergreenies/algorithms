# Linear search

> Linear search, also known as sequential search, is a simple searching algorithm used to find a target element in a list." It works by sequentially checking each element in the list until the desired element is found or until the end of the list is reached.

* ### Algorithm:

1. Start from the first element of the list.
2. Compare the target element with the current element.
3. If the current element matches the target element, the search is successful, and its index is returned.
4. If the current element does not match the target element, move to the next element in the list.
5. Repeat steps 2 to 4 until the target element is found or until the end of the list is reached.
5. If the target element is not found in the list, return a special value (e.g., -1) to indicate that the element is not present.

The linear search algorithm has a time complexity of `O(n) in the worst case`, where `n` is the number of elements in the list. It is suitable for small lists or when the elements are not sorted. However, for large lists, other algorithms like "binary search" are more efficient as they have a lower time complexity.

* ### Code snippets:

https://github.com/Evergreenies/go-algorithms/blob/b4a1cefd51c2172dd90fb99e93880e3e3445de63/algos/searching/001_linear_search.go#L1C1-L10C2
