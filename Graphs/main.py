"""
Mozna zaimplementowac dodatkowo A* algorytm i do implementacji mozna uzyc
heap napisany przez nas lub uzyc gotowej biblioteki heap.

Implementacja ma wyswietlac znaleziona droge na planszy lub informowac,
ze nie ma instniejacego rozwiazania grafu.
"""

import sys
from read_board import read_board
from dijkstra import dijkstra, NoPathFound, print_path


def main():
    if len(sys.argv) != 2:
        print("No path provided or too many arguments!")
        return
    board = read_board(sys.argv[1])
    try:
        path_result = dijkstra(board)
    except NoPathFound:
        print("No path was found for given graph!")
        return
    print_path(board, path_result)


if __name__ == "__main__":
    main()
