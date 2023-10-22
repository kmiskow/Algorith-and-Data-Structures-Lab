from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from selection_sort import selection_sort


def validate_sort(testing_array: list):
    for i in range(1, len(testing_array)):
        if testing_array[i] < testing_array[i-1]:
            return False
    return True


def test_pytest():
    assert True


def test_validate_sort_sorted_array():
    my_array = [1, 2, 3, 5, 5, 7, 8]
    assert validate_sort(my_array)


def test_validate_sort_unsorted_array():
    my_array = [1, 2, 3, 6, 4, 5, 7]
    assert not validate_sort(my_array)


def test_insertion_sort():
    my_array = [1, 4, 5, 7, 8, 2, 1]
    insertion_sort(my_array)
    assert validate_sort(my_array)


def test_bubble_sort():
    my_array = [1, 4, 5, 7, 8, 2, 1]
    bubble_sort(my_array)
    assert validate_sort(my_array)


def test_merge_sort():
    my_array = [1, 4, 5, 7, 8, 2, 1]
    merge_sort(my_array)
    assert validate_sort(my_array)


def test_quick_sort():
    my_array = [1, 4, 5, 7, 8, 2, 1]
    my_array = quick_sort(my_array)
    assert validate_sort(my_array)


def test_selection_sort():
    my_array = [1, 4, 5, 7, 8, 2, 1]
    selection_sort(my_array)
    assert validate_sort(my_array)
