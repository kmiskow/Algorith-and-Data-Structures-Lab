from plot_and_png import plotter


def load_text_as_array(file_path):
    word_list = []

    with open(file_path, 'r') as file_handle:
        for line in file_handle:
            line_list = line.split()

            for word in line_list:
                word_list.append(word)

    return word_list


def main():
    text = load_text_as_array("pan-tadeusz-unix.txt")
    plotter(text, 10000, 1000)


if __name__ == "__main__":
    main()
