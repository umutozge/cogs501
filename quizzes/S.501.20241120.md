`Quiz - 20/11 - COGS 501`
-------------------------
1. **[3pts]** Define a function that takes an integer `n` and a list `seq`, and returns a version of `seq` such that `n` is inserted right before the first element that is larger than `n`.

**Solution:**

```python
def insert_before_larger(n, seq):
    for i in range(len(seq)):
        if seq[i] > n:
            return seq[:i] + [n] + seq[i:]
    return seq + [n]
```

**Solution-2:**

```python
def insertbefore(n, seq):
    for x in seq:
        if x > n:
            i = seq.index(x)
            return seq[:i] + [n] + seq[i:]
    return seq + [n]
```

2. 🤑 **[2pts]** Solve the above problem by recursion.

**Solution:**

```python
def insertbefore_rec(n, seq):
    if not seq:
        return [n]
    elif seq[0] > n:
        return [n] + seq
    else:
        return seq[0:1] + insertbefore_rec(n, seq[1:])
```

**Solution-2:**

```python
def insbef(n, seq, acc = []):
    if not seq:
        return acc + [n]
    elif seq[0] > n:
        return acc + [n] + seq
    else:
        return insbef(n, seq[1:], acc + seq[0:1])
```
