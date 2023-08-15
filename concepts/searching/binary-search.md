## Binary Search Algorithm

> Binary search is an efficient searching algorithm used to find a target element in a sorted list. It works by repeatedly dividing the search interval in half and comparing the middle element with the target element. If the middle element matches the target, the search is successful, and the index of the element is returned. If the middle element is greater than the target, the search continues in the left half of the list. If the middle element is less than the target, the search continues in the right half of the list. The process repeats until the target element is found or until the search interval becomes empty.

### **Algorithm**

1. **Input**: The binary search algorithm takes two inputs:
   - A sorted list (or array) `arr`.
   - The target element `target` that we want to find in the list.

2. **Initialize Search Interval**: Set two pointers, `left` and `right`, to the first and last indices of the list, respectively. These pointers define the search interval.
3. **Loop Condition**: While `left` is less than or equal to `right`, repeat the following steps:

4. **Calculate Midpoint**: Compute the midpoint index `mid` as the average of `left` and `right`, rounded down to the nearest integer (e.g., `mid = (left + right) / 2`).

5. **Compare with Midpoint**: Compare the target element `target` with the element at index `mid` in the list `arr[mid]`.

6. **If Target is Found**: If `arr[mid]` is equal to `target`, return `mid`. The target element is found at index `mid`.

7. **If Target is Less Than `arr[mid]`**: If `target` is less than `arr[mid]`, set `right` to `mid - 1`. This means the target element, if present, must be in the left half of the search interval.

8. **If Target is Greater Than `arr[mid]`**: If `target` is greater than `arr[mid]`, set `left` to `mid + 1`. This means the target element, if present, must be in the right half of the search interval.

9. **Target Not Found**: If the loop ends and the target element is not found in the list, return a special value (e.g., -1) to indicate that the element is not present.

### **Pseudocode:**
```
function binarySearch(arr, target):
    left = 0
    right = length(arr) - 1

    while left <= right:
        mid = (left + right) / 2
        
        if arr[mid] == target:
            return mid
        else if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

**Time Complexity:**
- Binary search has a time complexity of `O(log n)`` because it halves the search space with each iteration.
- It is significantly faster than linear search, especially for large lists.

**Walk-Through Example:**

Suppose we have a sorted list `arr = [1, 3, 5, 7, 9, 11, 13]` and we want to find the index of the target element `target = 7`.

- Initial search interval: left = 0, right = 6
- First iteration: mid = (0 + 6) / 2 = 3, arr[mid] = 7 (match)
- The target element 7 is found at index 3.

**Practice:**
- Implement binary search in your preferred programming language.
- Solve a variety of problems that require binary search, such as finding the first and last occurrence of a target element or performing lower-bound and upper-bound searches.

**Explore Variants and Applications:**
- Explore variants of binary search, such as interpolation search and exponential search.
- Learn about its applications in other algorithms and data structures, such as binary search trees and divide-and-conquer algorithms.
