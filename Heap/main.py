from binary_heap import BinaryHeap
from NaryHeap import NaryHeap
from random import randint
from test_and_plot import get_build_time, plot_perf, get_pop_time


def pop_perf():
    rand_array = [randint(0, 1000000) for _ in range(100000)]
    performance = {}
    count_values = list(range(0, 100001, 10000))


    print("Binary Heap")
    performance_values = []
    for count in count_values:
        performance_values.append(get_pop_time(BinaryHeap(), rand_array[:count], 9))
        print(count)
    performance["Binary Heap"] = performance_values

    print("Quinary Heap")
    performance_values = []
    for count in count_values:
        performance_values.append(get_pop_time(NaryHeap(5), rand_array[:count], 9))
        print(count)
    performance["Quinary Heap"] = performance_values

    print("Septenary Heap")
    performance_values = []
    for count in count_values:
        performance_values.append(get_pop_time(NaryHeap(7), rand_array[:count], 9))
        print(count)
    performance["Septenary Heap"] = performance_values

    plot_perf(count_values, performance, False, "Pop Performance", "Heap size", "Time [s]")


def building_perf():
    rand_array = [randint(0, 1000000) for _ in range(100000)]
    performance = {}
    count_values = list(range(0, 100001, 10000))

    print("Binary Heap")
    performance_values = []
    for count in count_values:
        performance_values.append(get_build_time(BinaryHeap(), rand_array, count, 9))
        print(count)
    performance["Binary Heap"] = performance_values

    print("Quinary Heap")
    performance_values = []
    for count in count_values:
        performance_values.append(get_build_time(NaryHeap(5), rand_array, count, 9))
        print(count)
    performance["Quinary Heap"] = performance_values

    print("Septenary Heap")
    performance_values = []
    for count in count_values:
        performance_values.append(get_build_time(NaryHeap(7), rand_array, count, 9))
        print(count)
    performance["Septenary Heap"] = performance_values

    plot_perf(count_values, performance, False, "Building Performance", "Heap size", "Time [s]")


def main():
    print("Building performance checking")
    building_perf()
    print("Pop performance checking")
    pop_perf()


if __name__ == "__main__":
    main()
