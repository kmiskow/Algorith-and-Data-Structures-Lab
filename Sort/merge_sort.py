import sys


def merge_sort(word_list):
    if len(word_list) < 2:
        return

    mid = len(word_list)//2
    left = word_list[:mid]
    right = word_list[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            word_list[k] = left[i]
            i += 1
        else:
            word_list[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        word_list[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        word_list[k] = right[j]
        j += 1
        k += 1


def main(file_path):
    word_list = []

    with open(file_path, 'r') as file_handle:
        for line in file_handle:
            line_list = line.split()

            for word in line_list:
                word_list.append(word)

    merge_sort(word_list)
    print(word_list)


def testing():
    my_array = [1, 2, 3, 5, 4]
    merge_sort(my_array)
    print(my_array)


if __name__ == "__main__":
    main(sys.argv[1])
