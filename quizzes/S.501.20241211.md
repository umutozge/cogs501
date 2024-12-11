`Quiz - 11/12 - COGS 501`
-------------------------

1. **[3pts]** Define a function `remove_nth` with 3 arguments: `seq`, `item`,  `n`, which returns a version of `seq` where every `n`th occurrence of `item` is removed from `seq`.
   ```python
   >>> remove_nth([1,2,1,1,3,5,6,1,6,1,8], 1, 2)
   [1, 2, 1, 3, 5, 6, 6, 1, 8]
   ```

**Solution:**

```python
def remove_nth(seq, item, n):
    """remove every nth occurence of item from seq"""
    count = 0
    acc = []
    
    for i in seq:
        if i == item:
            count += 1
            if count == n:
                count = 0
            else:
                acc += [i]
        else:
            acc += [i]

    return acc
```

**Solution-2:**

```python
from functools import reduce

# Here is a solution with reduce

def remove_nth2(seq, item, n):
    return reduce(lambda acc, elm:
                  ((0, acc[1]) if acc[0] == (n - 1) else (acc[0]+1, acc[1]+[elm]) )
                  if elm == item else (acc[0], acc[1]+[elm]),
                 seq,
                 (0,[]))[1]
```

2. **[2pts]** The mean of `n` numbers is computed by dividing their sum by `n`. A running mean is a sequence of mean values updated as we see more data. Define a function that computes the running mean of a list of numbers. 
    ```python
    >>> run_mean([3, 5, 7, 9])
    [3.0, 4.0, 5.0, 6.0]
    ```

**Solution:**

```python
def run_mean(seq):
    count = 0
    sum = 0
    acc = []

    for i in seq:
        count +=1
        sum += i
        acc += [sum/count]

    return acc
```

**Solution-2:**

```python
from functools import reduce

def run_mean1(seq):
    return reduce(lambda acc, n: (acc[0]+[(acc[1]+n)/(acc[2]+1)],
                                  acc[1]+n,
                                  acc[2]+1),
                  seq,
                  ([],0,0))[0]
```

3. 🤑 **[1pt]** This point goes to the solution that does not use any statements for the previous question.

**Solution:**

```python
from functools import reduce

helper = lambda lst, x: lst + [(lst[-1] * len(lst) + x) / (len(lst) + 1)]

run_mean = lambda seq: reduce(helper, seq[1:], [float(seq[0])])
```
