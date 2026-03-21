class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        pass

        # could do backtracking, yes...
        # but we can do it faster with math 

        # the lexicographical minimum string
        # starts off "ababab..." 
        # and there are two choices for each
        # subsequent character... let's call
        # num chars present: m
        # num remaining chars: r
        # num strings that can be made with these chars: s = 2^r
        # so if k < s, we know the string so far is formed correctly 
        # when k becomes >= s, we have to flip the last character we
        # placed (either a or b, -> [a|b] or c) and subtract s from k

        result = "a"
        chars = ['a', 'b', 'c']
        if n == 1:
            if k > 3: return ''
            else: return chars[k - 1]
        s = 2 ** (n - 1)
        while len(result) < n:
            if k < s:
                if result and result[-1] == 'a': result += 'b'
                else: result += 'a'
                s >>= 1
            elif k == s:
                print(f"From result={result} for {n}, {k}, {s}: Finish with lexicographically largest string")
                if result and result[-1] == 'c': result += 'b'
                else: result += 'c'
            else:
                if len(result) == 1: 
                    if result[0] == 'c': return ''
                    else: result = chr(ord(result[0]) + 1)
                else: 
                    print(f"Result before flip for {n}, {k}, {s}:", result)
                    result = result[:-1] + {x for x in chars}.difference(result[-2:]).pop()
                    print(f"Result after flip for {n}, {k}, {s}:", result)
                k -= s
        return result

from leettest import TestRunner

TEST_CASES = [
    {'id': 1, 'n': 1, 'k': 3, 'expected': 'c'},
    {'id': 2, 'n': 1, 'k': 4, 'expected': ''},
    {'id': 3, 'n': 3, 'k': 9, 'expected': 'cab'},
    {'id': 4, 'n': 5, 'k': 2, 'expected': 'ababc'},
    {'id': 5, 'n': 10, 'k': 100, 'expected': 'abacbabacb'}, # actual: "abacbabab"
]

if __name__ == '__main__':
    runner = TestRunner(
        test_cases=TEST_CASES,
        solution_cls=Solution,
        method_name='getHappyString',
        input_keys=['n', 'k'],
        debug=True
    )
    runner.run_tests()