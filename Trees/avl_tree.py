from tree import Tree
from node import Node
from typing import Optional


class UnresolvedUnbalancedTree(Exception):
    pass


class avl_tree(Tree):
    def __init__(self, root: Optional["Node"] = None) -> None:
        super().__init__(root)

    def insert(self, new_value: "float") -> None:
        current_node = Node(new_value)
        if not self._root:
            self._root = current_node
            return
        self._root = self._insert(current_node, self._root)

    def balance(self):
        if not self._root:
            return 0
        return self._balance(self._root)

    def _balance(self, node) -> int:
        left_hight, right_hight = -1, -1
        if node.left:
            left_hight = node.left.height()
        if node.right:
            right_hight = node.right.height()
        return left_hight - right_hight

    def _insert(self, new_node: "Node", current_root: "Node") -> "Node":
        if new_node.value < current_root.value:
            if not current_root.left:
                current_root.left = new_node
                new_node.parent = current_root
            else:
                current_root.left = self._insert(new_node, current_root.left)
        elif new_node.value > current_root.value:
            if not current_root.right:
                current_root.right = new_node
                new_node.parent = current_root
            else:
                current_root.right = self._insert(new_node, current_root.right)

        balance = self._balance(current_root)

        if balance > 1:
            if new_node.value < current_root.left.value:
                return self._right_rotate(current_root)
            elif new_node.value > current_root.left.value:
                current_root.left = self._left_rotate(current_root.left)
                current_root.left.parent = current_root
                return self._right_rotate(current_root)
        if balance < -1:
            if new_node.value > current_root.right.value:
                return self._left_rotate(current_root)
            elif new_node.value < current_root.right.value:
                current_root.right = self._right_rotate(current_root.right)
                current_root.right.parent = current_root
                return self._left_rotate(current_root)
        return current_root

    @staticmethod
    def _left_rotate(root: "Node") -> "Node":
        child_node = root.right
        grandchild_node = child_node.left

        child_node.parent = root.parent
        root.parent = child_node
        child_node.left = root

        if grandchild_node:
            grandchild_node.parent = root
        root.right = grandchild_node

        return child_node

    @staticmethod
    def _right_rotate(root: "Node") -> "Node":
        child_node = root.left
        grandchild_node = child_node.right

        child_node.parent = root.parent
        root.parent = child_node
        child_node.right = root

        if grandchild_node:
            grandchild_node.parent = root
        root.left = grandchild_node

        return child_node


def main():
    my_tree = avl_tree()
    for i in range(15):
        my_tree.insert(i)
    my_tree.insert(15)
    print(my_tree.root)
    print(f"Balance of avl tree = {my_tree.balance()}")


if __name__ == "__main__":
    main()
