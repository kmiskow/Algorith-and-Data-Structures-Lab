class NaryHeap:
    def __init__(self, factor):
        self._factor = factor
        self._size = 0
        self._heap = []

    def size(self):
        return self._size

    def _swap(self, index):
        # return if no children
        if 1 + index * self._factor >= self._size:
            return
        # find max child
        max, max_index = self._heap[1 + index * self._factor], 1 + index * self._factor
        for i in range(2 + index*self._factor, 1 + (index + 1) * self._factor):
            if i >= self._size:
                break
            if self._heap[i] > max:
                max, max_index = self._heap[i], i
        if self._heap[index] >= self._heap[max_index]:
            return
        self._heap[index], self._heap[max_index] = self._heap[max_index], self._heap[index]
        self._swap(max_index)

    def push(self, value):
        self._heap.append(value)
        self._size += 1
        index = self._size - 1
        parent_index = (index - 1)//self._factor
        while parent_index >= 0:
            if self._heap[index] > self._heap[parent_index]:
                self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
                index = parent_index
                parent_index = (index - 1)//self._factor
            else:
                break

    def pop(self):
        if self._size == 0:
            raise IndexError("pop from empty heap")
        self._size -= 1
        if self._size == 1:
            return self._heap.pop()
        result = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._heap.pop()
        self._swap(0)
        return result

    def print(self):

        if self._size < 1:
            return print("Heap is Empty")
        levels = 0
        x = 0
        while x < self._size:
            x += self._factor**levels
            levels += 1
        max_index = 0
        max_width = ((self._factor)**(levels-1))*2
        print(str(self._heap[0]).center(max_width))
        for level in range(1, levels):
            seperator = '-'*((self._factor//2+1)*(levels-level))
            if level != levels-1:
                str_list = [str(x) for x in self._heap[max_index +
                                                      1:max_index + self._factor**level+1]]
                print(seperator.join(str_list).center(max_width))
                max_index = max_index + self._factor**level
            else:
                print(*self._heap[max_index + 1:], sep=' ')


def main():
    heap = NaryHeap(5)
    heap.push(1)
    heap.push(3)
    heap.push(2)
    heap.push(5)
    heap.push(12)
    heap.push(11)
    heap.push(20)
    heap.push(15)
    heap.push(30)
    heap.push(35)
    heap.push(10)
    print(heap._heap)
    while heap.size() > 0:
        heap.print()
        heap.pop()


if __name__ == "__main__":
    main()
