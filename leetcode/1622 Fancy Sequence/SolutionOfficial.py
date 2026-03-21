# We can combine several addAll operations and multAll operations into a single operation, 
# represented by the pair (a,b), which transforms any integer x into ax+b:

# Initially, (a,b)=(1,0).
# When we encounter the addAll(inc) operation, we increase b by inc.
# When we encounter the multAll(m) operation, we multiply both a and b by m.

# We use the array v to store the original sequence (that is, the values inserted by each append(val) operation). 
# We also use two arrays a and b to store the pairs described above, where (a_i,b_i) represents the result obtained 
# by condensing all operations before v_i is added to v.

# When we encounter the operation getIndex(idx), we consider both (a_idx, b_idx) and (a_l, b_l):

# Before v_idx is inserted into v, all previous operations can be condensed into (a_idx, b_idx).
# So far, all operations can be summarized as (a_l, b_l)

# Therefore, the operation applied to v_idx is equivalent to transforming the pair (a_idx, b_idx) into (a_l, b_l), 
# which we denote as (a_o, b_o). In other words, { a_idx ⋅ a_o = a_l b_idx ⋅ a_o + b_o = b_l }.

# The answer to the getIndex(idx) operation is therefore a_o ⋅ v_idx + b_o.

# How do we solve for a_o and b_o ? From the equations above, we obtain:
# { a_o = ( a_l / a_idx ) b_o = b_l − b_idx ⋅ ( a_l / a_idx ) }

# At first glance this seems straightforward, but we must note that after many addAll and multAll operations, 
# (a,b) may become very large, exceeding the range of integer types in most programming languages. 
# One solution would be to use high-precision arithmetic, but that would make the implementation significantly more complex.

# Fortunately, the problem only requires the result modulo 10 ** 9 + 7, 
# which allows us to use the concept of a modular multiplicative inverse.

# See https://leetcode.com/problems/fancy-sequence/editorial for a more detailed analysis
# of the prerequisite math concepts and the official solution. 

# Summary:
# Find the multiplicative inverse of an integer a modulo m (where m is prime, in this case 10e9 + 7) 
# a ⋅ a^(-1) ≡ 1 (mod m)
# -> a ⋅ a^(-1) = km + 1 for some integer k 
# -> a ⋅ a^(-1) - km = 1
# According to Bézout's identity, since a and m are coprime, there exist integers x and y such that ax + my = 1.
# gcd(a, m) = 1

# How to compute the multiplicative inverse a^(-1)? Use Fermat's little theorem:
# a^(m-1) ≡ 1 (mod m)
# -> a^(m-2) ≡ a^(-1) (mod m)
# We can compute a^(m-2) using fast exponentiation (also known as binary exponentiation or exponentiation by squaring)
# which runs in O(log(m)) time. For more details see https://leetcode.com/problems/powx-n/editorial/

class Fancy:

    def __init__(self):
        self.mod = 10**9 + 7
        self.v = list()
        self.a = [1]
        self.b = [0]

    # fast exponentiation
    def quickmul(self, x: int, y: int) -> int:
        return pow(x, y, self.mod)

    # multiplicative inverse
    def inv(self, x: int) -> int:
        return self.quickmul(x, self.mod - 2)

    def append(self, val: int) -> None:
        self.v.append(val)
        self.a.append(self.a[-1])
        self.b.append(self.b[-1])

    def addAll(self, inc: int) -> None:
        self.b[-1] = (self.b[-1] + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.a[-1] = self.a[-1] * m % self.mod
        self.b[-1] = self.b[-1] * m % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.v):
            return -1
        ao = self.inv(self.a[idx]) * self.a[-1]
        bo = self.b[-1] - self.b[idx] * ao
        ans = (ao * self.v[idx] + bo) % self.mod
        return ans