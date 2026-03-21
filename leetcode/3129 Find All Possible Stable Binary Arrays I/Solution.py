import math
# from math import factorial
from functools import cache

class Solution:
    @cache
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # for an array of size n
        # 2 options for first element
        # and next few up to limit
        # then 1 option iff all preceding
        # elements were like (2 scenarios, 0 and 1) 
        # else 2 options again 
        # until zero or one is exhausted 

        # the total # of ways to create an array
        # of length n with zero 0s and one 1s is
        # min(n!/zero!, n!/one!) == n!/max(zero,one)!

        # the number of these possible arrays with
        # at least one streak of consecutive like
        # characters with length > limit is... 

        # consider a streak that starts at the first index (index 0)
        # and has length of at least limit + 1
        # the streak is either all 1s or all 0s
        # the total # of ways this can happen is just the 
        # total number of ways to organize the subarray 
        # that follows, i.e. the subarray of length nl1 = n - limit - 1
        # using either limit + 1 less 0s (we can call that value zl1)
        # or limit + 1 less 1s (we can call it ol1)
        # so they total number of ways to create an array 
        # that uses the proper number of 1s and 0s but violates 
        # the streak limit from the very first character is 
        # nl1!/max(zl1,ones)! + nl1!/max(zeroes,ol1)!

        # now consider an invalid streak that *starts* at index 1
        # we do not want to duplicate any arrays that we already 
        # counted in the first scenario, so we have to assume 
        # that the streak *starts* at index 1 and no violations 
        # occurred prior to index 1 
        # in this scenario, that is relatively trivial: we just 
        # have to specify that the char at index 0 is an opp
        # to the chars composing the invalid streak
        # the invalid streak is again at least limit + 1 long
        # but the first char is also predetermined as the opp
        # so the first limit + 2 chars have been defined, 
        # and the number of ways to arrange the rest of the subarray
        # that follows is:
        # nl2!/max(zl2,ones-1)! + nl2!/max(zeroes-1,ol2)!

        # we can also use recursion to get the total number of valid 
        # ways to arrange the subarrays that precede and follow
        # the invalid streaks we're identifying ... might result 
        # in a stack overflow though?? can we simplify this math? 

        # what we have right now:
        # result = n!/max(zero,one)! 
        #       - sum([(n - limit - 1 - i)!/max(zeroes - limit - 1 - i, ones - i)!])
        #       - sum([(n - limit - 1 - i)!/max(zeroes - i, ones - limit - 1 - i)!])
        # all of these terms can be modulo'd *before* summing and diffing them 

        # return factorial(zero + one) // factorial(max(zero, one)) - sum([factorial(zero + one - limit - 1 - i) // factorial(max(zero - limit - 1 - i, one - i)) for i in range(min(zero, one) + 1)]) - sum([factorial(zero + one - limit - 1 - i) // factorial(max(zero - i, one - limit - 1 - i)) for i in range(min(zero, one) + 1)])

        def primeFactors(n: int) -> dict:
            # get prime factors of n
            result = {}
            for i in range(2, int(n ** 0.5) + 1):
                while not n % i: 
                    result[i] = result.get(i, 0) + 1
                    n // i
            if not result: result[n] = 1
            return result 

        def factorialOverFactorial(numeratorBase: int, denominatorBase: int) -> int:
            # better calc of numeratorBase!/denominatorBase!
            # ... except that this is just wrong 

            # pfnb = primeFactors(numeratorBase)
            # pfdb = primeFactors(denominatorBase) 
            # print(f"Prime factors of {numeratorBase} and {denominatorBase}:", pfnb, pfdb)
            # spf = { key: pfnb.get(key, 0) - pfdb.get(key, 0) for key in set(pfnb.keys() | pfdb.keys()) }
            # result = math.prod([key ** power for key, power in spf.items()])
            # return result 

            if denominatorBase > numeratorBase: raise ValueError("Denominator base must be less than or equal to numerator base")
            return math.prod(range(denominatorBase + 1, numeratorBase + 1))

        if zero > one: return self.numberOfStableArrays(one, zero, limit)

        n = zero + one
        # num = math.factorial(n)
        # denom = math.factorial(max(zero, one))
        # print(f"Factorial of {n} and {max(zero, one)}:", num, denom)
        # total = math.factorial(n) // math.factorial(max(zero, one))
        # total = num // denom
        total = factorialOverFactorial(n, max(zero, one))
        # print(f"Total and test values for {zero}, {one}, {limit}:", total, total_test)
        if limit >= n: return total 
        if zero <= 0 or one <= 0: return 0
        # if zero == 0 or one == 0: return 1
        print(f"Total for {zero}, {one}, {limit}:", total)
        lsac = []
        rsac = []
        for i in range(n - limit): # +1? -1? 
            # total -= factorialOverFactorial(n - limit - 1 - i, max(zero - limit - 1 - i, one - i))
            # total -= factorialOverFactorial(n - limit - 1 - i, max(zero - i, one - limit - 1 - i))
            # for j in range(min(i, n - limit - 1 - i)):
            #     total -= self.numberOfStableArrays()
            lsac.append(0)
            rsac.append(0)
            for j in range(min(i + 1, n - limit - i - 1)):
                # lsac[-1] += self.numberOfStableArrays(zero - limit - 1 - j, one - j, limit)
                # rsac[-1] += self.numberOfStableArrays(zero - j, one - limit - 1 - j, limit)
                lsac[-1] += self.numberOfStableArrays(j, i - j, limit)
                rsac[-1] += self.numberOfStableArrays(j, i - j, limit)
                # problem is here ^ the long side should have n - limit - 1 - j and the short side has i - j i think 
                # and also part of the problem is that only the left side should be required to be stable 
                # the right side can be any arrangement of the remaining 0s and 1s 
                # another problem i realized: this is a combination problem, not a permutation problem
                # think of the array as a collection of indexes and we are picking the locations to place the 0s 
                # in any order 
        print(f"LSAC and RSAC for {zero}, {one}, {limit}:", lsac, rsac)
        total -= sum([x * y for x, y in zip(lsac, rsac[::-1])])
        return total


        # violZero = sum([math.factorial(n - limit - 1 - i) // math.factorial(max(zero - limit - 1 - i, one - i)) for i in range(min(zero, one) + 1)])
        # violOne = sum([math.factorial(n - limit - 1 - i) // math.factorial(max(zero - i, one - limit - 1 - i)) for i in range(min(zero, one) + 1)])
        # return total - violZero - violOne

        ### Hint 1: Let dp[a][b][c = 0/1][d] be the number of stable arrays 
        # with exactly a 0s, b 1s and consecutive d value of c’s at the end.

        ### Hint 2: Try each case by appending a 0/1 at last to get the inductions.

# test cases from 3129 readme:
# 1. zero = 1, one = 1, limit = 2 -> 2
# 2. zero = 1, one = 2, limit = 1 -> 1
# 3. zero = 3, one = 3, limit = 2 -> 14

from leettest import TestRunner

TEST_CASES = [
    {"id": 1, "zero": 1, "one": 1, "limit": 2, "expected": 2},
    {"id": 2, "zero": 1, "one": 2, "limit": 1, "expected": 1},
    {"id": 3, "zero": 3, "one": 3, "limit": 2, "expected": 14},
]

if __name__ == "__main__":
    runner = TestRunner(
        test_cases=TEST_CASES,
        solution_cls=Solution,
        method_name="numberOfStableArrays",
        input_keys=["zero", "one", "limit"],
        debug=True,
    )
    runner.run_tests()