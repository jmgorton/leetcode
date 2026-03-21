# from math import sum
from operator import add, mul

class Fancy:

    # ops = []
    # vals = []
    # pre = {}
    MOD = 10 ** 9 + 7

    def __init__(self):
        self.ops = []
        # self.vals = []
        self.els = 0
        self.pre = {}

    def append(self, val: int) -> None:
        # # self.pre[len(self.vals)] = (val, len(self.ops))
        # self.pre[self.els] = (val, len(self.ops))
        # # self.vals.append(val)
        # self.els += 1

        # here, we have to store the inverse value of val,
        # by applying the modular inverse of all current operations
        # in O(1) time (we will be able to then "unwrap" 
        # all subsequent operations in O(1) time during getIndex)
        pass

    def addAll(self, inc: int) -> None:
        # self.ops.append((add, inc))

        # here, we have to update the inverse value according to the new 
        # addition operation, which is just subtracting inc from the inverse value
        pass

    def multAll(self, m: int) -> None:
        # self.ops.append((mul, m))

        # here, we have to update the inverse value according to the new 
        # multiplication operation, which is multiplying the inverse value by the modular inverse of m
        pass

    def getIndex(self, idx: int) -> int:
        # # if idx >= len(self.vals): return -1
        # if idx >= self.els: return -1
        # # result = self.pre[idx][0] if idx in self.pre else self.vals[idx]
        # # it = self.pre[idx][1] if idx in self.pre else 0
        # result, it = self.pre[idx] 
        # for op, val in self.ops[it:]:
        #     result = op(result, val)
        # # result %= 10e9 + 7
        # result %= self.MOD
        # self.pre[idx] = (result, len(self.ops))
        # return result

        # here, we have to apply all operations to the inverse value in O(1) time,
        # which is just applying the accumulated effect of all operations to it
        pass
    
    ### TLE at 105/107
    ### Key insight (from discussion board):
    # There’s a more elegant idea.
    # Think about it: if we append a new element after performing a series of operations, 
    # can we "roll back" its state to what it would have been if we had added it before these operations?

    # For example:

    # fancy.append(2);   // [2]  
    # fancy.addAll(3);   // [5]  
    # fancy.append(7);   // [5, 7]  
    # If we roll back the number 7 to the moment when 2 was added, we get 7 - 3 = 4. 
    # That is, we store the element in its original form and apply 
    # the accumulated effect of all operations to it during getIndex.

    # Thus:

    # When append is called, we store the "inverse" value 
    # that would have existed before all accumulated operations.
    # When getIndex is called, we apply all accumulated operations in O(1) time.
    # Separately, it’s worth noting that in the problem, 
    # all calculations are performed modulo 10^9 + 7. This is a prime number, 
    # which allows the use of modular arithmetic inverses 
    # (particularly for "rolling back" via multiplication). 
    # The modulus is needed here to prevent numbers from growing too large, 
    # but it also provides a tool for correct inverse operations.

    # See: Extended Euclidean Algorithm for finding modular inverses


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)