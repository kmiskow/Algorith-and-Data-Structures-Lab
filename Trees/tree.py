from node import Node
from typing import Optional


class RootChangeError(Exception):
    pass


class Tree:
    def __init__(self, root: Optional["Node"] = None):
        self._root = root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, _):
        raise RootChangeError("Cannot change root of a tree!")

    def find(self, value: int, node: Node = None) -> Node:
        if node is None:
            node = self.root

        if value == node.value:
            return node

        if value < node.value:
            if node.left is not None:
                return self.find(value, node.left)
            return None

        if node.right is not None:
            return self.find(value, node.right)

    def min_value(self, node: Node = None) -> Node:
        if node is None:
            node = self.root

        if node.left is None:
            return node

        return self.min_value(node.left)

    def insert(self, value: int, node: Node = None) -> None:
        if node is None:
            node = self.root

        if value < node.value:
            if node.left is not None:
                self.insert(value, node.left)
            else:
                node.left = Node(value, None, None, node)
        else:
            if node.right is not None:
                self.insert(value, node.right)
            else:
                node.right = Node(value, None, None, node)

    def delete(self, value, root: Node = None) -> None:
        if root is None:
            root = self.root

        node = self.find(value, root)

        if node.left is None and node.right is None:    # no children
            if node.value < node.parent.value:
                node.parent.left = None
            else:
                node.parent.right = None

            node.parent = None
        elif node.left is not None and node.right is None:  # only left child
            node.left.parent = node.parent

            if node.value < node.parent.value:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
        elif node.left is None and node.right is not None:  # only right child
            node.right.parent = node.parent

            if node.value < node.parent.value:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
        else:
            # Node with two children
            # Get the inorder successor (smallest in the right subtree)
            inorder = self.min_value(node.right)

            # Copy the inorder successor's content to this node
            node.value = inorder.value

            # Delete the inorder successor
            self.delete(inorder.value, node.right)

    def __str__(self) -> str:
        def traverse(node, level=0):
            if node is None:
                return ''

            left = traverse(node.left, level + 1)
            right = traverse(node.right, level + 1)

            return f'{right}{level * "  "}{node.value}\n{left}'

        return traverse(self.root)


def main():
    node = Node(50)
    bst = Tree(node)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print(bst)
    print("\n---------------\n")
    bst.delete(30)
    print(bst)
    print("\n---------------\n")
    bst.delete(40)
    print(bst)
    print("\n---------------\n")
    bst.delete(50)
    print(bst)


if __name__ == "__main__":
    main()
