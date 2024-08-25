def insert(arr: list[int], item: int) -> list[int]:
    if not arr:
        return []

    length = len(arr)
    if item > arr[length - 1]:
        arr.append(item)

        return arr

    index = length - 1
    arr.append(0)
    while index >=0 and arr[index] > item:
        arr[index + 1] = arr[index]
        index -= 1

    arr[index+1] = item
    return arr


print(insert([1, 2, 3, 4, 5, 8, 9, 10], 6))
print(insert([1, 2, 3, 4, 5, 8, 9, 10], 11))
print(insert([1, 2, 3, 4, 5, 8, 9, 10], 0))
