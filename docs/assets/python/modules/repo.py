def fibonacci(n):
    """Compute the nth Fibonacci number, for n >= 2."""
    pred, curr = 0, 1
    k = 2
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

def sum_square_naturals(n):
    """Return the sum of the squares of the first n  natural numbers.

    >>> sum_square_naturals(0)
    0
    >>> sum_square_naturals(3)
    14
    >>> sum_square_naturals(5)
    55
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k * k, k + 1
    return total

def collatz(n):
    """The Collatz function

    >>> collatz(0)
    0
    >>> collatz(3)
    10
    >>> collatz(8)
    4
    >>> collatz(-8)
    -4
    """
    if n%2==0:
        return n//2     # // instead of / for an integer result
    else:
        return 3*n+1

def print_collatz_sequence(n):
    """Print the Collatz sequence seeded by n.

    >>> print_collatz_sequence(8)
    8
    4
    2
    1
    """
    while n != 1:
        print(n)
        n = collatz(n)
    print(1)  # Print the last element of the sequence

def collatz_length(n):
    """The length of the Collatz sequence seeded by n (n and 1 are included)

    >>> collatz_length(8)
    4
    >>> collatz_length(3)
    8
    """
    counter = 1
    while n != 1:
        counter += 1
        n = collatz(n)
    return counter

def largest_random(k):
    """Return the largest of k ranndom integers between 1 and 1000000."""
    from random import randint
    largest_so_far = 0
    counter = 1
    while counter <= k:
        r = randint(1, 1000000)
        if r > largest_so_far:
            largest_so_far = r
        counter += 1
    return largest_so_far

def largest_collatz_length(k):
    """The largest Collatz length for the seeds between 1 and k."""
    largest_so_far = 0
    counter = 1
    while counter <= k:
        current_length = collatz_length(counter)
        if current_length > largest_so_far:
            largest_so_far = current_length
        counter += 1
    return largest_so_far

def maximal_collatz_seed(k):
    """The largest seed between 1 and k that produces the largest Collatz length."""
    largest_length = 0
    seed_with_largest_length = 0
    counter = 1
    while counter <= k:
        current_length = collatz_length(counter)
        if current_length > largest_length:
            largest_length = current_length
            seed_with_largest_length = counter
        counter += 1
    return seed_with_largest_length

def fibonacci(n):
    """Return the n-th Fibonacci number (n>=1).

    >>> fibonacci(1)
    0
    >>> fibonacci(2)
    1
    >>> fibonacci(8)
    13
    """
    if n <= 2:
        return n - 1
    count = 3
    prev, curr = 0, 1
    while count <= n:
        prev, curr = curr, prev + curr
        count += 1
    return curr

def fibonacci_ps(n):
    """Return the n-th Fibonacci number (n>=1).

    >>> fibonacci_ps(1)
    0
    >>> fibonacci_ps(2)
    1
    >>> fibonacci_ps(8)
    13
    """
    from funcutils import proc_seq
    def increment(x): return x + 1
    def alive(x): return x <= n
    def update(store, n):
        return (store[1], store[0] + store[1])
    return proc_seq(1, increment, alive, update, (-1,1))[1]  


def factorial(n):
    """Return the factorial of n (n>=0).

    >>> factorial(0)
    1
    >>> factorial(5)
    120
    >>> factorial(7)
    5040
    """
    store = 1
    k = 1
    while k <= n:
        store *= k
        k += 1
    return store

def first_non_decreasing_triplet():
    """Return the first non-decreasing triplet of random integers between 1 and 100.

    >>> import random
    >>> random.seed(48)
    >>> first_non_decreasing_triplet()
    (17, 72, 92)
    """
    from random import randint
    m, n, p = randint(1, 100), randint(1, 100), randint(1, 100)
    while not (m <= n and  n <= p):  # not (x <= y <= z) for short
        m, n, p = n, p, randint(1, 100)
    return (m, n, p)

def largest_collatz(n):
    """Return the largest number in the Collatz sequence seeded by n.

    >>> largest_collatz(8)
    8
    >>> largest_collatz(3)
    16
    """
    largest_so_far = n
    while n != 1:
        n = collatz(n)
        if n > largest_so_far:
            largest_so_far = n
    return largest_so_far

def dec2bin(n):
    """Convert n to binary representation."""
    if n == 0:
        return "0"
    acc = ""
    while n > 0:
        acc = str(n % 2) + acc
        n = n // 2
    return acc

def proc_seq(n, sequencer, alive, update, init):
    """Process a sequence of numbers.

    sequencer: function that produces the next number in the sequence
    alive: function that tests whether to continue processing
    update: function that updates the state
    init: initial state

    >>> def sequencer(n): return n - 1
    >>> def alive(n): return n > 0
    >>> def update(state, n): return state + n
    >>> proc_seq(5, sequencer, alive, update, 0)
    15
    """
    state = init
    while alive(n):
        state = update(state, n)
        n = sequencer(n)
    return state

def sum_digits(n):
    """Return the sum of the digits of n in decimal representation.

    >>> sum_digits(0)
    0
    >>> sum_digits(123)
    6
    >>> sum_digits(4096)
    19
    """
    def sequencer(n): return n // 10
    def alive(n): return n > 0
    def update(state, n): return state + (n % 10)
    return proc_seq(n, sequencer, alive, update, 0)

def sum_even_collatz(n):
    """Return the sum of the even numbers in the Collatz sequence seeded by n.

    >>> sum_even_collatz(8)
    14
    >>> sum_even_collatz(3)
    40
    """
    def sequencer(n): return collatz(n)
    def alive(n): return n != 1
    def update(state, n):
        if n % 2 == 0:
            return state + n
        else:
            return state
    return proc_seq(n, sequencer, alive, update, 0)





from collatz import collatz
from funcutils import proc_seq

# def collatz_direction_changes(n):
#     """Return the number of direction changes in the Collatz sequence seeded by n.
# 
#     >>> collatz_direction_changes(8)
#     0
#     >>> collatz_direction_changes(7)
#     9
#     """
#     def alive(n): return n > 1
#     def update(store, new):
#         if ((store[1] < store[2] and store[2] > new)
#             or
#             (store[1] > store[2] and store[2] < new)):
#             return (store[0] + 1, store[2], new)
#         else:
#             return (store[0], store[2], new)
#     initial_store = (0, n, n)
#     final_store = proc_seq(n, collatz, alive, update, initial_store)
#     return final_store[0]

def turning_point(x,y,z):
    """Retrurn True if y is a turning_point from increasing to decreasing
       or vice versa.

    >>> turning_point(1,2,3)
    False
    >>> turning_point(3,2,1)
    False
    >>> turning_point(1,3,2)
    True
    >>> turning_point(3,1,2)
    True
    >>> turning_point(2,2,3)
    False
    """
    return (z - y) * (y - x) < 0

# def collatz_direction_changes(n):
#     """Return the number of direction changes in the Collatz sequence seeded by n.
# 
#     >>> collatz_direction_changes(8)
#     0
#     >>> collatz_direction_changes(7)
#     9
#     """
#     def alive(n): return n > 1
#     def update(store, new):
#         count, two_back, one_back = store
#         if turning_point(two_back, one_back, new):
#             return (count + 1, one_back, new)
#         else:
#             return (count, one_back, new)
#     initial_store = (0, n, n)
#     final_store = proc_seq(n, collatz, alive, update, initial_store)
#     return final_store[0]

def collatz_direction_changes(n):
    """Return the number of direction changes in the Collatz sequence seeded by n.

    >>> collatz_direction_changes(8)
    0
    >>> collatz_direction_changes(7)
    9
    """
    return proc_seq(n,
                    collatz,
                    lambda n: n > 1,
                    lambda store, new: (store[0] + int(turning_point(store[1], store[2], new)),
                                        store[2],
                                        new),
                    (0, n, n))[0]

# def mod(a, b):
#    """Compute a mod b for a>=0.
# 
#    >>> mod(10, 3)
#    1
#    >>> mod(9, 9)
#    0
#    >>> mod(3, 10)
#    3
#    """
#    while a >= b:
#        a = a - b
#    return a
# 

# def mod(a, b):
#    """Compute a mod b for a>=0.
# 
#    >>> mod(10, 3)
#    1
#    >>> mod(9, 9)
#    0
#    >>> mod(3, 10)
#    3
#    """
#    return proc_seq(a,
#                    seq=lambda x: x - b,
#                    alive=lambda x: x>=0,
#                    update =  lambda store, x : x,  
#                    init = 0)


# def mod(a,b):
#     """Compute a mod b.
# 
#     >>> mod(10, 3)
#     1
#     >>> mod(9, 9)
#     0
#     >>> mod(3, 10)
#     3
#     >>> mod(-7,3)
#     2
#     """
#     if a >= 0:
#         while a >= b:
#             a = a - b
#         return a
#     else:
#         while a < 0:
#             a = a + b
#         return a
# 

def divides(a,b):
    """Return True if a divides b.

    >>> divides(3,9)
    True
    >>> divides(2,9)
    False
    >>> divides(9,2)
    False
    >>> divides(5,0)
    True
    """
    assert a != 0, "divides: first argument must be non-zero"
    a,b = abs(a), abs(b)
    while b >= a:
        b = b - a
    return  b == 0

def mod(a,b):
    """Compute a mod b.

    >>> mod(10, 3)
    1
    >>> mod(9, 9)
    0
    >>> mod(3, 10)
    3
    >>> mod(-7,3)
    2
    """
    return proc_seq(a,
                    seq=lambda x: x -1,
                    alive=lambda x: not divides(b,x),
                    update= lambda store, x : store +1,
                    init = 0)


