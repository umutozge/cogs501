`Quiz - 27/11 - COGS 501`
-------------------------
1. **[2pts]** The function `bubble` takes an integer `n` and a sequence `seq` of integers and inserts `n` into `seq` at the furthest possible position where there is no integer that is greater than `n` before it. Assume you have `bubble` defined. Use it and `reduce` to sort a given sequence of integers.

**Solution:**

```python
def bubble_sort(seq):
    return reduce(lambda acc, n: bubble(n, acc), seq, [])
```

**Solution-2:**

```python
bubble_sort = lambda seq: reduce(lambda acc, n: bubble(n, acc), seq, [])
```

2. **[2pts]** Define your own version of `filter` which returns a boolean mask rather than the filtered list. E.g.:

```python
>>> filter_boolean_mask(lambda x: x > 2, [1,2,4,2,4,4])
[False, False, True, False, True, True]
```

**Solution:**

```python
def filter_boolean_mask(func, lst):
    return list(map(func, lst))
```

**Solution-2:**

```python
def filter_boolean_mask(func, lst):
    acc = []

    for x in lst:
        acc += [func(x)]

    return acc
```

**Solution-3:**

```python
# same as the one above
def filter_boolean_mask(func, lst):
    return [func(x) for x in lst]
```

3. 🤑 **[1pt]** You get this bonus if you solve the above problem without using
   any statements.

**Solution:**

```python
filter_boolean_mask = lambda func, lst: list(map(func, lst))
```
