from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        trie = {}
        for word in dictionary:
            node = trie
            for ch in word:
                if ch not in node: node[ch] = {}
                node = node[ch] 
        
        def traverse(node: dict, word: str, index: int, edits: int) -> bool:
            if edits < 0: return False
            if index == len(word): return True

            found = False
            if word[index] in node:
                found = traverse(node[word[index]], word, index + 1, edits)

            if not found:
                for child in node.keys():
                    if child == word[index]: continue
                    found = found or traverse(node[child], word, index + 1, edits - 1)
                    if found: break
            
            return found 
        
        result = []
        for word in queries:
            if traverse(trie, word, 0, 2): result.append(word)
        return result 