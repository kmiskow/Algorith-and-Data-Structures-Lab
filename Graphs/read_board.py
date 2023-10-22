from typing import List, Union


class ReadingBoardError(Exception):
    pass


def read_board(file_path: str) -> List[List[Union[int, str]]]:
    with open(file_path, "r") as file_handle:
        board_raw = file_handle.readlines()
    column_count = max(len(row.rstrip()) for row in board_raw)
    board_result = []
    for row in board_raw:
        row_list = []
        for char in row.rstrip():
            if char in ['X', ' ']:
                row_list.append(char)
                continue
            row_list.append(int(char))
        row_list += [' '] * (column_count - len(row_list))
        if len(row_list) != column_count:
            raise ReadingBoardError("read_board function did something wrong")
        board_result.append(row_list)

    return board_result


if __name__ == "__main__":
    print(read_board("Graphs\\board1.txt"))
