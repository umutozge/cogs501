COGS 501 - :calendar: 13/11 - Fall 2024
-----------------------------------------------

#### Reading
* Stavely, Section 6.4

#### Checklist 
* Define a `lambda` function that takes two lists and returns their concatenation where the longer list precedes the shoter one. The function `len` maps a list to its length.
* Define a `lambda` function that takes 2 one-argument functions and an argument, and returns the function that gives the largest result when applied to the argument.
* Take a list of integers and returns the element which seeds the longest Collatz sequence. 
* Take the name of a `csv` file as string and return the contents as a list of tuples. Each tuple represents a row. Remember that the first line in a `csv` file does not belong to the data, it just names the columns (=fields) in the table. You may find the functions `split` and `strip` useful in your task.

    For now test your solutions with a simple file like:
    ```
    A,B,C
    1,2,3
    4,5,6
    7,8,9
    ```
    and variations of it. Once we equip ourselves with some skills and tools, we will have interesting datasets in the coming weeks.

* Let us call the type of the object returned by the previous program a `Sheet`. We want each column of a sheet to contain only a single type of value. (Two columns may differ in the type of data they contain, but a single column should be type-homogenous.) Take a `Sheet` and return `True` if the sheet is well-formed in the above sense, and return `False` otherwise. You can check the type of a value by the function `type`.
