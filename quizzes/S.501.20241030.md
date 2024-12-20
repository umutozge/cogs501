Quiz (30/10) - COGS 501
------------------------------------
1. **[2pts]** Define the Collatz function in Python.

**Solution:**

```python
def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1
```
   
2. **[4pts]** Define a function that takes an integer `n` greater than or equal to
   1, and returns the number of times one encounters a number that exceeds `n`
   while reducing `n` to 1 by the Collatz function.

**Solution:**
```python
def col_exceeds(n):
    count = 0
    n1 = n # This is our original n

    while n != 1:
        if n > n1: # If the number is larger than our original n, we add 1 to our count.
            count += 1
        n = collatz(n)

    print(count) # Here we print how many we counted within the while loop.
```

**Solution-2:**
```python
def col_exceeds(n):
    count = 0
    n1 = n # This is our original n

    while n != 1:
        if n > n1: # If the number is larger than our original n, we add 1 to our count.
            count += 1
        if n % 2 == 0: # In case you don't have the Collatz function already defined.
            n = n/2
        else:
            n = 3*n + 1

    print(count) # Here we print how many we counted within the while loop.
```
   
4. 🤑 **[4pts]** One way to decide whether a positive integer `m` is divisible by another
   positive integer `n` is to repeatedly subtract `n` from `m` until you arrive at `0` or
   a negative integer. If you reached `0` then, `m` is divisible by `n`; if you
   skipped `0` and arrived at a negative integer, then `m` is not divisible by
   `n`. Define a recursive function that takes `m` and `n` as arguments and
   returns `1` if `m` is divisible by `n` and returns `0` otherwise. (A
   non-recursive solution gets the half.)

**Solution:**
```python

def divisible(m, n):
    """Return 1 if m is divisible by n, else return 0"""
    if m > n:
        return divisible((m - n), n)
    else:
        print(1 if m - n == 0 else 0)
```

**Non-recursive solution:**
```python
def divisible(m, n):
    while m >= n:
        m -= n
    print(1 if m == 0 else 0)
```
