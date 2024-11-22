`Quiz - 06/11 - COGS 501`
-------------------------
1. **[2pts]** Take a list of integers and return the largest. Do not use any built-in `max` function. Use a `for` loop.

**Solution:**
```python
def largest_int(numbers):
    largest_n = numbers[0] # before using a for loop, save the first integer in the list as the largest (so far)
    
    for x in numbers[1:]: # check the rest of the list one by one.
        if x > largest_n: # If the element that is being checked is larger than the saved integer,
            largest_n = x # Then save that larger integer as our largest.
        # If the element that is being checked is not larger than the saved integer, do nothing.
    
    return largest_n # After the loop has ended, return the largest integer.
```

2. **[3pts]** Take an integer and a list of integers, count the number of occurrences of the first argument in the second. No `for/while` loop, use recursion.

**Solution:**
```python
def occurrence_no(target, numbers):
    if not numbers: # base case: when the list is empty, return 0
        return 0
    elif target == numbers[0]: # if the first element matches the target, add 1 to the result
        return 1 + occurrence_no(target, numbers[1:]) # continue with the rest of the list
    else: # if the first element does not match the target, do not add anything to the result
        return 0 + occurrence_no(target, numbers[1:]) # just continue with the rest of the list
```

3. 🤑 **[2pt]** Solve the first problem by recursion.

**Solution:**
```python
def largest_integer(numbers):
    if len(numbers) == 1: # base case: if there is only one integer left in the list, return it.
        return numbers[0]
    elif numbers[0] > numbers[-1]: # if the first element is larger than the last element,
        return largest_integer(numbers[:-1]) # then continue without the last element.
    else: # if not, that means the last element was larger than the first,
        return largest_integer(numbers[1:]) # continue without the first element.
```

**Another solution:**
```python
def find_largest(numbers):
    if len(numbers) == 1: # base case: if there is only one integer left in the list, return it.
        return numbers[0]
    
    largest_of_rest = find_largest(numbers[1:])
    return numbers[0] if numbers[0] > largest_of_rest else largest_of_rest # compare the first element with the largest of the rest
```
