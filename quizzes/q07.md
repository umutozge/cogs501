`Quiz - 13/11 - COGS 501`
-------------------------
1. **[2pts]** Define a function `filter`, which takes a function `func` and a list
   `seq` and returns a list where all the elements `seq` that return `False` for
   `func` are removed. Use a loop.
1. **[3pts]** Define a `lambda` function that takes a 2-argument function `f` and
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
1. 🤑 **[2pt]** Solve the first problem by recursion.
