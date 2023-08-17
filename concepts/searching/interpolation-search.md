## Interpolation Search:
> Interpolation Search is a searching algorithm that works well for uniformly distributed sorted arrays. It's particularly useful when the elements in the array are not evenly spaced, as it estimates the position of the desired element based on its value.

**How Interpolation Search Works:**
1. Calculate the position of the desired element using the interpolation formula:
   - `pos = low + ((key - arr[low]) / (arr[high] - arr[low])) * (high - low)`
   - `low` and `high` are the indices of the current search range.
   - `key` is the value you're searching for.
   - `arr[low]` and `arr[high]` are the values at indices `low` and `high` respectively.

2. Compare the `key` with the estimated value at position `pos`:
   - If `key` matches the estimated value, return `pos`.
   - If `key` is smaller, narrow the search range to the left side of `pos`.
   - If `key` is larger, narrow the search range to the right side of `pos`.

3. Repeat the above steps until the `key` is found or the search range becomes empty.

**Python Implementation:**
```python
def interpolationSearch(arr, key):
    low, high = 0, len(arr) - 1
    
    while low <= high and key >= arr[low] and key <= arr[high]:
        if low == high:
            if arr[low] == key:
                return low
            return -1
        
        pos = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        if arr[pos] == key:
            return pos
        elif arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1
            
    return -1
```

**Time Complexity:**
- Best case: O(1) - occurs when the element being searched is found at the estimated position.
- Worst case: O(n) - occurs when elements are not uniformly distributed and the search range is reduced by a constant fraction in each iteration.

**Applications of Interpolation Search:**
1. **Temperature Sensor Readings:** Interpolation Search can efficiently locate a specific temperature reading in a sorted array of temperature data, where temperatures are evenly distributed.
   
2. **Time Series Data:** Interpolation Search is suitable for finding specific timestamps in time series datasets where data points are approximately evenly spaced.

3. **Log Files Analysis:** For logs sorted by timestamp, Interpolation Search helps locate events within certain time intervals for debugging and analysis.

4. **Missing Value Detection:** Interpolation Search can identify the position where a missing value should be inserted in a sorted array.

5. **Economic Data Analysis:** It's applicable for quickly finding specific economic indicators in sorted datasets collected at regular intervals.

Interpolation Search is an effective algorithm in scenarios where data distribution is even. It might not perform optimally for clustered or irregularly spaced data.

**Challenges**
1. **Two Sum**
- Problem Statement: Given an array of integers `nums` and an integer target, return indices of the two numbers such that they add up to the target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
- Example: 
  - Input: nums = [2, 7, 11, 15], target = 9
  - Output: [0, 1]
  - Explanation: nums[0] + nums[1] equals 9, so the indices are 0 and 1.

2. **Maximum Subarray**
- Problem Statement: Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
- Example:
  - Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
  - Output: 6
  - Explanation: The contiguous subarray [4, -1, 2, 1] has the largest sum = 6.
 