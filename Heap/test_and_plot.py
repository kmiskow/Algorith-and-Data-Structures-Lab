import gc
import time
from copy import deepcopy
import matplotlib.pyplot as plot
from typing import Union, Dict, List
from binary_heap import BinaryHeap
from NaryHeap import NaryHeap


def get_build_time(heap: Union[BinaryHeap, NaryHeap], array, array_count, repeat=0):
    result = 0
    for _ in range(1 + repeat):
        gc_old = gc.isenabled()
        gc.disable()
        new_heap = deepcopy(heap)
        start = time.perf_counter()
        for value in array[:(array_count)]:
            new_heap.push(value)
        stop = time.perf_counter()
        if gc_old:
            gc.enable()
        result += (stop - start)
    return result / (1 + repeat)


def get_pop_time(heap: Union[BinaryHeap, NaryHeap], array, repeat=0):
    for value in array:
        heap.push(value)
    result = 0
    for _ in range(1 + repeat):
        gc_old = gc.isenabled()
        gc.disable()
        new_heap = deepcopy(heap)
        start = time.perf_counter()
        for _ in range(heap.size()):
            new_heap.pop()
        stop = time.perf_counter()
        if gc_old:
            gc.enable()
        result += (stop - start)
    return result / (1 + repeat)


def plot_perf(x, y: Dict[str, List[int]], save=True, title="Title", xlabel="X", ylabel="Y"):
    plot.title(title, fontsize='16')	 # title
    for name, values in y.items():
        plot.plot(x, values, label=name)	 # plot the points
    plot.xlabel(xlabel, fontsize='13')  # adds a label in the x axis
    plot.ylabel(ylabel, fontsize='13')  # adds a label in the y axis
    plot.legend(loc='best')  # creates a legend to identify the plot
    plot.grid()  # shows a grid under the plot
    plot.show()
    if save:
        # saves the figure in the present directory
        plot.savefig(title+'_'+xlabel+'_'+ylabel+'.png')


def main():
    test_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(get_build_time(BinaryHeap(), test_array, 5))


if __name__ == "__main__":
    main()
