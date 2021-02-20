class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = [None, None]

    def __str__(self):
        result = []

        if self.children[0] is not None:
            result.append(self.children[0].__str__())

        result.append(str(self.value))

        if self.children[1] is not None:
            result.append(self.children[1].__str__())

        return ' '.join(result)


class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = BinaryTreeNode(value)
        else:
            self._add(self.root, value)

    def _add(self, root, value):
        if value <= root.value:
            child = 0
        else:
            child = 1

        if root.children[child] is None:
            root.children[child] = BinaryTreeNode(value)
        else:
            self._add(root.children[child], value)

    def remove(self, value):
        # It's easier to implement remove as a function that returns the
        # modified subtree.
        self.root = self._remove_and_return(self.root, value)

    def _remove_and_return(self, root, value):
        assert root is not None

        if value > root.value:
            assert root.children[1] is not None
            root.children[1] = self._remove_and_return(root.children[1], value)
            return root
        elif value < root.value:
            assert root.children[0] is not None
            root.children[0] = self._remove_and_return(root.children[0], value)
            return root
        else:
            if root.children[0] is not None:
                predecessor = self._max_node(root.children[0])
                root.value = predecessor.value
                root.children[0] = self._remove_and_return(
                    root.children[0], predecessor.value)
                return root
            elif root.children[1] is not None:
                successor = self._min_node(root.children[1])
                root.value = successor.value
                root.children[1] = self._remove_and_return(
                    root.children[1], successor.value)
                return root
            else:
                return None

    def _max_node(self, root):
        assert root is not None

        max_node = root
        while max_node.children[1] is not None:
            max_node = max_node.children[1]

        return max_node

    def _min_node(self, root):
        assert root is not None

        min_node = root
        while min_node.children[0] is not None:
            min_node = min_node.children[0]

        return min_node

    def __str__(self):
        return self.root.__str__()
