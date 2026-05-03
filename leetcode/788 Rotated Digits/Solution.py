class Solution:
    def rotatedDigits(self, n: int) -> int:
        # a number is valid if it contains only 0, 1, 2, 5, 6, 8, and 9
        # a number is invalid if it contains a 3, 4, or 7
        # a valid number is good if it contains a 2, 5, 6, or 9 

        # now thinking through multi-digit numbers...
        # we should think about them in blocks based on number of digits 

        # e.g. all 1-digit cases are enumerated above (exactly 4 good) 
        # 2-digit cases require that there are *no* 3/4/7 and
        # *at least one* 2/5/6/9

        # for a block of n-digit numbers, the ratio of valid:total is (.7)^n 
        # and the ration of good:valid is 1 - ((3/7)^n) 

        # now handling a sub-section of a multi-digit block -- imagine n=2345 
        # we have to handle all 1-, 2- and 3- digit numbers via formula (above)
        # but we also have to handle 4-digit numbers from 1000 to 2345
        # meaning we have to handle all 4-digit numbers that start with 1, and 
        # the section 2000 to 2345

        # given the first digit is known, there are three buckets to consider
        # 1. the first number is invalid -> the whole block is invalid: 0
        # 2. the first number is valid -> two sub-branches:
        #   a. the first number is good -> the remaining digits only need be valid 
        #   b. the first number is valid -> the remaining digits must be good 

        # pre-compute good and valid based on number of digits 
        # dig = math.floor(math.log(n, 10)) + 1
        # print(dig) 
        # valid = [0] * dig
        # good = [0] * dig
        # valid[0] = 0.7
        # good[0] = 
        # return None

        def getGoodCount(hi, lo=0, good=False) -> int:
            result = 0 
