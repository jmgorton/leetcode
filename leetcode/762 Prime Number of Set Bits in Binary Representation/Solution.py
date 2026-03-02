class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # every power of two has exactly one set bit
        # after every power of two, there is one number
        # that follows that has two set bits (unless...
        # another power of two follows, i.e. 1 -> 2)

        # we're going about that wrong 
        # for every gap between powers of two, every
        # combination of the lsbs will exist 
        # this is n choose k, with formula:
        # n! / k! (n - k)! 
        # the inputs for this problem go up to 1M,
        # which is roughly 20 bits 

        # 1: 0001
        # 2: 0010
        # 3: 0011
        # 4: 0100
        # 5: 0101
        # 6: 0110
        # 7: 0111
        # 8: 1000
        # 9: 1001
        # 10: 1010
        # 11: 1011
        # 12: 1100
        # 13: 1101
        # 14: 1110
        # 15: 1111

        # relevant prime numbers (given the bits we might use for the input)
        p = [2, 3, 5, 7, 11, 13, 17, 19]

        # calculate all combos of n choose k ... we probably only 
        # need to calculate the values of p as k choices 
        # and since we're calculating between powers of two,
        # and assuming that the first bit is definitely set,
        # we actually want to consider only the lesser bits 
        # and calculate k's one less than the prime values above 

        # to do that, we might even want to memoize the factorials 
        fact = [1]
        for i in range(1, 21): fact.append(fact[-1] * i) # python has no overflow 

        choose = [[None] * 21 for _ in range(21)]
        for i in range(21):
            # for j in p:
            #     jp = j - 1
            for jp in range(21):
                # calculate i choose jp ... could keep numerator and denominator
                # as sets or something and simplify before multiplying/dividing ... 
                # getting prime factorizations of num/denom and canceling out 

                # brute force (ish):
                choose [i][jp] = fact[i] // (fact[jp] * fact[i - jp]) if i >= jp else None
        
        def getTotalCountWithNBitsSetFromOneToValIncl(val: int, n: int) -> int:
            if val <= 0: return 0
            if n <= 0: return 0
            bitSet = 20
            x = 2 ** bitSet
            while x >= val: 
                x >>= 1
                bitSet -= 1
            result = getTotalCountWithNBitsSetFromOneToValIncl(val - x, n - 1) # + (choose[bitSet][n] if bitSet >= n else 0)
            while bitSet > 0:
                result += choose[bitSet][n - 1] if choose[bitSet][n - 1] else 0
                bitSet -= 1
            return result 

        # if left != 0:
        #     return self.countPrimeSetBits(0, right) - self.countPrimeSetBits(0, left)


        return sum([getTotalCountWithNBitsSetFromOneToValIncl(right, pv) - getTotalCountWithNBitsSetFromOneToValIncl(left, pv) for pv in p])
    
import sys; sys.path.append(".")
from TestRunner import TestRunner

# print(sys.path)


TEST_CASES = [
    {"id": 1, "left": 6, "right": 10, "expected": 4},
    {"id": 2, "left": 10, "right": 15, "expected": 5},
]


if __name__ == "__main__":
    runner = TestRunner(
        test_cases=TEST_CASES,
        solution_cls=Solution,
        method_name="countPrimeSetBits",
        input_keys=["left", "right"],
    )
    runner.run_tests()