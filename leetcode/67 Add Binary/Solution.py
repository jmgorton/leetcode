from itertools import zip_longest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""
        for ab, bb in zip_longest(a[::-1], b[::-1], fillvalue="0"):
            ls = int(ab) + int(bb) + carry
            result += f"{ls & 1}"
            carry = ls >> 1
        if carry: result += "1"
        return result[::-1]