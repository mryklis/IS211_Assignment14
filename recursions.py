from fractions import gcd
import inspect


def rec_fib(n):
    # adapted from http://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence-in-python
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    else:
        return n


# print inspect.getsource(gcd)
# I looked at the built in function code to determine the correct function.
def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

# def compareTo(s1, s2):


if __name__ == '__main__':
    # expect 8
    print rec_fib(6)
    # expect 10
    print gcd(10, 20)
