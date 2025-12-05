from funcutils import proc_seq

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

def collatz_sequence(n):
    """Return the Collatz sequence seeded by n as a list.

    >>> collatz_sequence(1)
    [1]
    >>> collatz_sequence(8)
    [8, 4, 2, 1]
    """
    return proc_seq(n, collatz,  lambda x: x > 1, lambda state, x: state + [x], []) + [1]

def collatz_length(n):
    """The length of the Collatz sequence seeded by n (n and 1 are included)

    >>> collatz_length(8)
    4
    >>> collatz_length(3)
    8
    """
    return proc_seq(n, collatz, lambda x: x > 1, lambda state, x: state + 1, 1)

def largest_in_collatz_sequence(n):
    """Return the largest integer in the Collatz sequence seeded by n.

    >>> largest_in_collatz_sequence(11)
    52
    >>> largest_in_collatz_sequence(27)
    9232
    """
    def alive(n): return n > 1
    return proc_seq(n, collatz, alive, max, 0)
