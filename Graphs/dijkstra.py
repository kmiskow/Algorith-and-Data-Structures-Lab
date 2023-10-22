from typing import List, Union, Tuple
from colorama import Back
from node_binary_heap import Heap


class NoPathFound(Exception):
    pass


def print_path(board: List[List[Union[int, str]]], dijkstra_path: List[Tuple[int, int]]) -> None:
    for row_index, row in enumerate(board):
        for column_index, value in enumerate(row):
            if (column_index, row_index) not in dijkstra_path:
                print(Back.RESET + str(value), end='')
            else:
                print(Back.GREEN + str(value), end='')
        print(Back.RESET + '')


def neighbors(index: Tuple[int, int], rows: int, columns: int) -> Tuple[int, int]:
    """Generator for neighbors of current index."""
    neighbor_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(4):
        x, y = index
        neighbor_diff_x, neighbor_diff_y = neighbor_list[i]
        x += neighbor_diff_x
        y += neighbor_diff_y
        if x < 0 or x >= columns:
            continue
        if y < 0 or y >= rows:
            continue
        yield x, y


def min_dist_index(que: Heap, visited_board: List[List[bool]]) -> Tuple[int, int]:
    while not que.empty():
        _, (x, y) = que.pop()
        # If index was already visited skip it and pop new index
        if visited_board[y][x] is False:
            return x, y
    raise NoPathFound("Que is empty!")


def dijkstra(board: List[List[Union[int, str]]]) -> List[Tuple[int, int]]:
    board_rows = len(board)
    board_columns = len(board[0])

    # previous 2d array holds index of closes node. Can backtrack steps from start to finish
    previous = [[None for _ in range(board_columns)] for _ in range(board_rows)]
    # True if node was already tested
    # walls are marked as visited in next step to skip their evaluation
    visited = [[False for _ in range(board_columns)] for _ in range(board_rows)]

    # Create distance 2d array that holds distance to starting node
    # Distance is set to infinity
    distance = []
    start_index = ()
    for row_index, row in enumerate(board):
        distance_row = []
        for column_index, value in enumerate(row):
            if value == 'X':
                if not start_index:
                    start_index = (column_index, row_index)
                    distance_row.append(0)
                    continue
            if value == ' ':
                visited[row_index][column_index] = True  # Set walls as visited so they are not evaluated in next steps
            distance_row.append(float('inf'))
        distance.append(distance_row)

    # Heap holding (distance, (x index, y index))
    que = Heap()

    x, y = start_index
    while True:
        visited[y][x] = True

        # if 'X' we found end, break loop
        if board[y][x] == 'X' and (x, y) != start_index:
            break

        curr_distance = distance[y][x]
        for x_nbr, y_nbr in neighbors((x, y), board_rows, board_columns):
            # skip visited neighbor
            if visited[y_nbr][x_nbr]:
                continue

            neighbor_distance = distance[y_nbr][x_nbr]
            neighbor_step_cost = board[y_nbr][x_nbr]
            if neighbor_step_cost == 'X':  # stepping on end is free
                neighbor_step_cost = 0

            # if recorded distance lower then current: continue
            if neighbor_distance <= neighbor_step_cost + curr_distance:
                continue

            distance[y_nbr][x_nbr] = neighbor_step_cost + curr_distance
            previous[y_nbr][x_nbr] = (x, y)
            que.push((distance[y_nbr][x_nbr], (x_nbr, y_nbr)))

        x, y = min_dist_index(que, visited)

    dijkstra_path = []
    while True:
        dijkstra_path.append((x, y))
        if previous[y][x] is None:
            break
        x, y = previous[y][x]
    return dijkstra_path
