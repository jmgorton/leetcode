from itertools import zip_longest

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # print([f"{i}: {c}" for i, c in enumerate(encodedText)])
        # print(encodedText.split())
        # print([x for x in zip(*encodedText.split())])
        # print(''.join([''.join(x) for x in zip_longest(*encodedText.split(), fillvalue='')]))
        cols = len(encodedText) // rows
        rowVals = [encodedText[i*cols+i:(i+1)*cols] for i in range(rows)]
        # print(rowVals)
        # print([x for x in zip_longest(*rowVals, fillvalue='')])
        return ''.join([''.join(x) for x in zip_longest(*rowVals, fillvalue='')]).rstrip()