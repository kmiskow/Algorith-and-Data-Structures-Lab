class BinaryHeap:
    def __init__(self) -> None:
        self._nodes = [0]

    def size(self):
        return len(self._nodes)

    def push(self, value: int):
        self._nodes.append(value)

        i = self.size() - 1
        while i > 1 and self._nodes[i // 2] < self._nodes[i]:
            self._nodes[i // 2], self._nodes[i] = self._nodes[i], self._nodes[i // 2]

            i = i // 2

    def pop(self) -> int:
        if self.size() <= 1:
            return None

        result = self._nodes[1]
        if self.size() == 2:
            self._nodes.pop()
            return result
        self._nodes[1] = self._nodes.pop()

        i = 1
        while 2 * i + 1 < self.size() and self._nodes[i] < max(self._nodes[2 * i], self._nodes[2 * i + 1]):
            if self._nodes[2 * i] >= self._nodes[2 * i + 1]:
                self._nodes[2 * i], self._nodes[i] = self._nodes[i], self._nodes[2 * i]
                i = i * 2
            else:
                self._nodes[2 * i + 1], self._nodes[i] = self._nodes[i], self._nodes[2 * i + 1]
                i = i * 2 + 1

        return result

    def print(self):
        levels = []
        i = 1
        while i < self.size():
            level = self._nodes[i:2 * i]
            levels.append(level)
            i *= 2

        max_level_width = len(" ".join(str(val) for val in self._nodes[1:]))
        for i, level in enumerate(levels):
            level_str = ""
            for j, val in enumerate(level):
                if val != 0:
                    level_str += str(val).center(max_level_width // (2 ** i))
                else:
                    level_str += " " * (max_level_width // (2 ** i))

                if j != len(level) - 1:
                    level_str += " " * ((max_level_width // (2 ** i)) - len(str(val)))

            print(level_str.center(max_level_width))


def main():
    heap = BinaryHeap()
    heap.push(10)
    heap.push(9)
    heap.push(5)
    heap.push(8)
    heap.push(4)
    heap.push(7)

    heap.print()
    print(f"After pop'ing: {heap.pop()}")
    heap.print()
    print(heap._nodes)


if __name__ == "__main__":
    main()
