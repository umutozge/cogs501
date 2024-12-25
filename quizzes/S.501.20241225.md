`Quiz - 25/12 - COGS 501`
-----------------------

1. **[2pts]** Define a function that takes a data frame, and a column name and returns the list of values in the given column. A data frame is a list of dictionaries as in the exercises.

**Solution:**

```python
def column_values(df, col):
    acc = []
    for x in df:
        if col in x:
            acc += [x[col]]
    return acc
```

2. **[2pts]** Define a function that generates a random bit string of length `length`. Remember that a bit string is a string (or list) of `0`s and `1`s. Assume you have a two place function `randint` which produces a random number including and between its two integer arguments.

**Solution:**

```python
def random_bit_string(length):
    acc = []
    for i in range(length):
        acc += [randint(0, 1)]
    return acc
```

3. 🤑 **[2pts]** You get one extra credit if you can solve the problems with lambda functions using no statements.

**Solution for Q1:**

```python
col_values = lambda df, col: [x[col] for x in df]
```

**Solution for Q2:**

```python
rand_bit_string = lambda length: [randint(0, 1) for i in range(length)]
```
