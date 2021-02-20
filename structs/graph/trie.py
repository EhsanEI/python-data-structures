class TrieNode():
    def __init__(self):
        self.complete = False
        self.children = {}


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def add(self, string):
        node = self.root
        for c in string:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.complete = True

    def lookup(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]

        array = []
        child_strings = self._all_strings(node)
        array.extend([''.join([prefix, string]) for string in child_strings])
        return array

    def _all_strings(self, node):
        array = []

        if node.complete:
            array.append('')

        for key, child in node.children.items():
            child_strings = self._all_strings(child)
            array.extend([''.join([key, string]) for string in child_strings])

        return array

    def __str__(self):
        return self._all_strings(self.root).__str__()
