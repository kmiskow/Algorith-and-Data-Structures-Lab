class Heap:
    def __init__(self):
        self._size = 0
        self._heap = []

    def empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def _swap(self, index):
        # return if no children
        if 1 + index * 2 >= self._size:
            return
        # min child
        min, min_index = self._heap[1 + index * 2], 1 + index * 2
        if 2 + index * 2 < self._size and self._heap[2 + index * 2] < min:
            min, min_index = self._heap[2 + index * 2], 2 + index * 2
        if self._heap[index] < self._heap[min_index]:
            return
        self._heap[index], self._heap[min_index] = self._heap[min_index], self._heap[index]
        self._swap(min_index)

    def push(self, value):
        self._heap.append(value)
        index = self._size
        self._size += 1
        parent_index = (index - 1)//2
        while parent_index >= 0:
            if self._heap[index] < self._heap[parent_index]:
                self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
                index = parent_index
                parent_index = (index - 1)//2
            else:
                break

    def pop(self):
        if self._size == 0:
            raise IndexError("pop from empty heap")
        self._size -= 1
        if self._size == 0:
            return self._heap.pop()
        result = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._heap.pop()
        self._swap(0)
        return result


def main():
    h = Heap()
    h.push((5, 1))
    h.push((6, 2))
    h.push((4, 4))
    h.push((3, 3))
    h.push((1, 5))
    print(h.pop())
    print(h.pop())
    print(h.pop())
    print(h.pop())
    print(h.pop())
    pass


if __name__ == "__main__":
    main()