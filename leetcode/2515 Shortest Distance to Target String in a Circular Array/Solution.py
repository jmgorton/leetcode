from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        # could opt by starting at startIndex and potentially avoiding
        # having to search the entire list of words
        # but the simpler solution that works here is to just search
        # the whole thing and return the min

        indices = { i if v == target else None for i, v in enumerate(words) }
        indices.discard(None)

        n = len(words)
        return min([min((startIndex - i + n) % n, (i - startIndex + n) % n) for i in indices]) if indices else -1