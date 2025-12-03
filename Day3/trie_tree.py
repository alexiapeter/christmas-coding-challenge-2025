"""
   Leetcode problem: 208. Implement Trie(Prefix Tree) - medium
   Author: Peter Alexia
   Description:
    A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

   Date: 3.dec.2025
"""
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


if __name__ == "__main__":
    trie = Trie()
    print("Nested Dictionary Trie Initialized ")

    trie.insert("apple")
    print("Inserted 'apple'")
    print(f"Search 'apple': {trie.search('apple')}")
    print(f"Search 'app':   {trie.search('app')}")
    print(f"StartsWith 'app': {trie.startsWith('app')}")
    trie.insert("app")
    print("Inserted 'app'")
    print(f"Search 'app':   {trie.search('app')}")