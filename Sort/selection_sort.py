import sys


def selection_sort(word_list):
    for i in range(len(word_list)):
        min_index = i

        for j in range(i+1, len(word_list)):
            if word_list[j] < word_list[min_index]:
                min_index = j

        if word_list[min_index] < word_list[i]:
            word_list[i], word_list[min_index] = word_list[min_index], word_list[i]

    return word_list


def main(file_path):
    word_list = []

    with open(file_path, 'r') as file_handle:
        for line in file_handle:
            line_list = line.split()

            for word in line_list:
                word_list.append(word)

    word_list = selection_sort(word_list)
    print(word_list)


if __name__ == "__main__":
    main(sys.argv[1])
