def insertion_sort(array):
    j = None
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1
