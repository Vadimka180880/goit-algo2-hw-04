class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, key, value):
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.value = value

    def _get_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def keys(self):
        result = []

        def dfs(node, prefix):
            if node.value is not None:
                result.append(prefix)
            for char, child in node.children.items():
                dfs(child, prefix + char)

        dfs(self.root, "")
        return result