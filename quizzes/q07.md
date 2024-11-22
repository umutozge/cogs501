`Quiz - 13/11 - COGS 501`
-------------------------
1. **[2pts]** Define a function `filter`, which takes a function `func` and a list
   `seq` and returns a list where all the elements `seq` that return `False` for
   `func` are removed. Use a loop.

**Solution:**

```python
def filter(func, seq):
    result = [] # this will be "filtered" list.
    for item in seq: # go through every item in 'seq'
        if func(item): # when an item if applied to the function, if the result is true,
            result += [item] # (if the result is true), then keep it in the 'result' list
        # since there is no else statement here, if the result was false, it wasn't added to the 'result' list
    return result
```
   
2. **[3pts]** Define a `lambda` function that takes a 2-argument function `f` and
   returns a function `g`, where `g` does exactly what `f` does but receives its
   arguments in the opposite order of `f`. For instance let's assume you name
   your `lambda` function `foo`. and let `bar = lambda x,y: x**y`. `foo(bar)(2,3)` must return `9`, where `bar(2,3)` would return `8`.
   ```python
   >>> bar = lambda x, y: x**y
   >>> foo = <YOUR LAMBDA FUNCTION HERE>
   >>> bar(2,3)
   8
   >>> foo(bar)(2,3)
   9
   ```

**Solution:**

```python
foo = lambda f: lambda x, y: f(y, x)
"""
This is lambda function called 'foo'.
It takes a function called 'f' as its argument.
'lambda x, y' part says that 'f' must be a function that takes two arguments.
Then, the order of 'x' and 'y' is changed. That is our 'foo' function.
"""
```
   
3. 🤑 **[2pt]** Solve the first problem by recursion.

**Solution:**

```python
def filter(func, seq):
    if not seq:  # base case: if the list 'seq' is empty, return it (and end recursion)
        return []
    if func(seq[0]):  # when the first item of 'seq' is applied to the function, if the result is true,
        return [seq[0]] + filter(func, seq[1:])  # (if the result is true), then keep it and do the same thing to the rest of the list
        # so that means we traverse the list by removing the first item of the list and keeping it in the result or not keeping in the result
    else: # (if the result was false)
        return filter(func, seq[1:]) # skip the first element and continue with the rest of the list
    # at the end, we reach an empty list (the base case) and all the true-returning items are concatenated.
```
