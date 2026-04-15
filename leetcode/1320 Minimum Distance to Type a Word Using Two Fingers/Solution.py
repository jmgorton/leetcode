class Solution:
    def minimumDistance(self, word: str) -> int:
        pass

    # different from a two traveling salesmen problem
    # instead of all characters on the keyboard, we have to hit each character
    # in the word in order. 

    # decisions made:
    # 1. where the fingers start initially (26 x 26/25 possibilities)
    # 2. which finger to use for each letter (2 per letter) 
    #   - for this one, we have to consider the possibilities of where 
    #   - each finger was before this, which is influenced by all previous decisions. 