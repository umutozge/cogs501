`Quiz - 4/12 - COGS 501`
-------------------------

1. <s>**[2pts]**</s> (cancelled) Find the second largest integer in a list of integers using `reduce`.

**Solution:**

```python
from functools import reduce

reducer = lambda lst, n: [n, lst[0]] if n > lst[0] else ([lst[0], n] if n > lst[1] else lst[:2])

find_second_largest = lambda seq: reduce(reducer, seq[2:], ([seq[0], seq[1]] if seq[0] > seq[1] else [seq[1], seq[0]]))[1]
```

**Solution without lambda functions:**

```python
from functools import reduce

def reducer(lst, n):
    if n > lst[0]:
        return [n, lst[0]]
    elif n > lst[1]:
        return [lst[0], n]
    else:
        return lst[:2]

def find_second_largest(seq):
    initial = [seq[0], seq[1]] if seq[0] > seq[1] else [seq[1], seq[0]]
    return reduce(reducer, seq[2:], initial)[1]
```

2. **[2pts]** You will take as input one-argument function `f` and two equal sized sequences of integers `seq1` and `seq2`. You will return a sequence of integers of the same size as `seq1` and `seq2` such that each position of the result sequence is occupied by the element at the same position from `seq1` or `seq2` depending on which of them gives a higher value for `f`.

**Solution:**

```python
def map_list(f, x, y):
    if len(x) != len(y):
        raise ValueError("The lists must be of the same length.")
    
    acc = []

    for i in range(len(x)):
        if f(x[i]) > f(y[i]):
            acc += [x[i]]
        else:
            acc += [y[i]]

    return acc
```

3. 🤑 **[1pt]** This point goes to the solution that does not use any statement for the previous question.

**Solution:**

```python
map_list = lambda f, seq1, seq2: list(map((lambda x, y: x if f(x) > f(y) else y), seq1, seq2))
```
