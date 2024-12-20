`Quiz - 18/12 - COGS 501`
-------------------------

1. **[3pts]** Define a function `flatten` that takes a possibly nested list and returns the flattened version.
    ```python
    >>> flatten([[3,9], 5, [7, [9]]])
    [3, 9, 5, 7, 9]
    ```

**Solution with a loop+recursion:**

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

**Solution without recursion:**

```python
def flatten2(lst): # checks whatever is in the stack and removes the outermost brackets one by one

    flattened = []
    stack = [lst]

    while stack:
        current = stack[-1]
        stack = stack[:-1]
        if type(current) is list:  # at the start, whatever is in the stack is definitely a list,
            stack += current[::-1] # so, we reverse that list and concatenate it with the stack, which removes the outermost brackets of the list
                                   # this means that, in the first step, we just reversed the list :)
                                   # then we add the non-list items to "flattened" one by one
        else:
            flattened += [current]

    return flattened
```

**Solution without any loops:**

```python
def flatten3(lst):
    if not lst:
        return lst
    elif type(lst[0]) is list:
        return flatten3(lst[0]) + flatten3(lst[1:])
    else:
        return lst[:1] + flatten3(lst[1:])
```

**Solution in one line: (same as above)**

```python
flatten4 = lambda lst: lst if not lst else (flatten4(lst[0]) + flatten4(lst[1:]) if type(lst[0]) is list else lst[:1] + flatten4(lst[1:]))
```

**Solution with reduce:**

```python
from functools import reduce

helper = lambda acc, item: acc + (flatten5(item) if type(item) is list else [item])

flatten5 = lambda nested_list: reduce(helper, nested_list, [])
```

2. **[3pts]** A palindrome is a string whose reverse is equal to itself: `aba`, `a`, `baab`, `ey edip adanada pide ye`, and so on. Define a function that maps a string to `True` or `False` depending whether it is a palindrome or not.

**Solution with a while loop:**

```python
def palindrome(s):
    while len(s) > 1:
        if s[0] == s[-1]:
            s = s[1:-1]
        else:
            return False
    return True
```

**Solution with a for loop:**

```python
def palindrome4(s):
    if len(s) < 2:
        return True
    
    for i in range(len(s) // 2):
        if not (s[i] == s[-(i + 1)]):
            return False
    
    return True
```

**Solution with recursion:**

```python
def palindrome2(s):
    if len(s) < 2:
        return True
    elif s[0] == s[-1]:
        return palindrome2(s[1:-1])
    else:
        return False
```

**Solution with a lambda function (recursive):**

```python
palindrome3 = lambda s: True if len(s) < 2 else (palindrome3(s[1:-1]) if s[0] == s[-1] else False)
```

**Solution with recursion in a different way:**

```python
def palindrome5(string, i = 0):
    if i >= len(string) // 2:
        return True
    elif string[i] == string[-(i + 1)]:
        return palindrome5(string, i + 1)
    else:
        return False
```

