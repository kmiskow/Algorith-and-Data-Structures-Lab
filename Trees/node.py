from typing import Optional


class NodeValueChangeError(Exception):
    pass


class Node:
    def __init__(self,
                 value: int,
                 left: Optional["Node"] = None,
                 right: Optional["Node"] = None,
                 parent: Optional["Node"] = None
                 ) -> None:
        self._value = value
        self._left = left
        self._right = right
        self._parent = parent

    def __str__(self) -> str:
        return_string = f"{self._value}"
        if self._left:
            left_string = str(self._left).replace('\n', "\n| ")
            return_string += f"\n+l: {left_string}"
        if self._right:
            right_string = str(self._right).replace('\n', "\n| ")
            return_string += f"\n+r: {right_string}"
        return return_string

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def left(self) -> "Node":
        return self._left

    @left.setter
    def left(self, new_left: "Node") -> None:
        self._left = new_left

    @property
    def right(self) -> "Node":
        return self._right

    @right.setter
    def right(self, new_right: "Node") -> None:
        self._right = new_right

    @property
    def parent(self) -> "Node":
        return self._parent

    @parent.setter
    def parent(self, new_parent: "Node") -> None:
        self._parent = new_parent

    def height(self) -> int:
        if not self._right and not self._left:
            return 0

        right, left = 0, 0
        if self._right:
            right = self._right.height()
        if self._left:
            left = self._left.height()

        return max(left, right) + 1
