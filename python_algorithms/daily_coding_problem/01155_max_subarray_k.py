"""
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the
maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not
need to store the results. You can simply print them out as you compute them.
"""

from collections import deque


def max_subarray_k(arr: list[int], k: int) -> None:
    if not arr or k <= 0:
        return

    dq = deque()
    for index in range(len(arr)):
        if dq and dq[0] < index - k + 1:
            dq.popleft()

        while dq and arr[dq[-1]] < arr[index]:
            dq.pop()

        dq.append(index)
        if index >= k - 1:
            print(arr[dq[0]], end=" ")

    print()


max_subarray_k([10, 5, 2, 7, 8, 7], 3)
