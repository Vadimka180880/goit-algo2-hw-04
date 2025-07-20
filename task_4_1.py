from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Патерн має бути рядком")

        count = 0
        for word in self.keys():
            if word.endswith(pattern):
                count += 1
        return count

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Префікс має бути рядком")

        node = self._get_node(prefix)
        return node is not None

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

print("Слова, що закінчуються на 'e':", trie.count_words_with_suffix("e"))
print("Чи є префікс 'app'? ->", trie.has_prefix("app"))
print("Чи є префікс 'bat'? ->", trie.has_prefix("bat"))
print("✅ Усі тести пройдено успішно.")