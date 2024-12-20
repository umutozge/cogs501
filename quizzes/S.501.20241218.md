`Quiz - 18/12 - COGS 501`
-------------------------

1. **[3pts]** Define a function `flatten` that takes a possibly nested list and returns the flattened version.
    ```python
    >>> flatten([[3,9], 5, [7, [9]]])
    [3, 9, 5, 7, 9]
    ```

**Solution:**

```python
def flatten(lst):

    flattened = []
    
    for item in lst:
        if type(item) is list:
            flattened += flatten(item)
        else:
            flattened += [item]
    
    return flattened
```

**Solution-2:**

```python
def flatten(lst):

    flattened = []
    stack = [lst]

    while stack:
        current = stack[-1]
        stack = stack[0:-1]
        if type(current) is list:
            stack += current[::-1]
        else:
            flattened += [current]

    return flattened
```

I will add more solutions when I have more time (Ecenur)

2. **[3pts]** A palindrome is a string whose reverse is equal to itself: `aba`, `a`, `baab`, `ey edip adanada pide ye`, and so on. Define a function that maps a string to `True` or `False` depending whether it is a palindrome or not.

**Solution:**

```python
def palindrome(str):

    str = list(str)
    
    while str != []:
        if len(str) == 1:
            return True
        elif str[0] == str[-1]:
            str = str[1:-1]
        else:
            return False
    return True
```
