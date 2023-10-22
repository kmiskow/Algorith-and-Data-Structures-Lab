class QuintaryHeap:
    def __init__(self):
        self._heap = []

    def insert(self, new_elem):
        self._heap.append(new_elem)
        if len(self._heap) == 1:
            return
        node_index = (len(self._heap) - 1)
        parent_index = node_index // 5
        while parent_index >= 0:
            if self._heap[node_index] <= self._heap[parent_index]:
                return
            self._heap[node_index], self._heap[parent_index] = self._heap[parent_index], self._heap[node_index]
            node_index = parent_index
            parent_index = (node_index - 1) // 5


def main():
    heap = QuintaryHeap()
    heap.insert(2)
    heap.insert(6)
    heap.insert(7)
    heap.insert(10)
    heap.insert(3)
    heap.insert(11)

    print(heap._heap)


if __name__ == "__main__":
    main()
