def quick_sort(arr):
    # 1 element array
    if len(arr) < 2:
        return arr

    left, right = [], []
    pivot_index = len(arr)//2
    pivot = arr[pivot_index]
    for i in range(len(arr)):
        if pivot_index == i:
            continue
        if arr[i] <= pivot:
            left.append(arr[i])  # lesser part
        else:
            right.append(arr[i])  # smaller part
    return quick_sort(left) + [pivot] + quick_sort(right)  # combine lists (lesser,greater and pivot)
