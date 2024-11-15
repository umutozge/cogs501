COGS 501 - :calendar: 20/11 - Fall 2024
-----------------------------------------------

#### Reading
* No reading, just coding, a lot of coding... 

#### Checklist 
* Define a function that takes an integer `n` and a list `seq`, and returns a
    version of `seq` such that `n` is inserted right before the first element
    that is larger than `n`. Try two versions, one with a loop and one with
    recursion. 
* Define a function that takes a sequence of integers and returns its sorted
    version in ascending order. There are many ways to sort a list, but for this
    problem make use of your solution to the previous problem. Again, try to
    solve this with and wihtout recursion.
* Now you know how to read a `csv` file into a `Table` (let's change the name
    `Sheet` to `Table`). Slightly change your representation of a `Table` by
    making it a 2-tuple which consists of the list of column names and the list
    of lists or tuples (our old representation of a `Table` ). You can get the list of
    column names by the first line in the file.
* Define a function `get_column` which takes a `Table` and an `Adress` as
    arguments. `Address` may either be an integer or a string. If the user
    provides an integer, then you will treat it as an index, and if the user
    provides a string, then you will treat it as a column name. Return the
    column wanted by the user.
* Define a  3-place function `get_item` that takes a `Table`, an integer (to be
    treated as the row index), and an integer (column index) or a string (column
    name). Return the item wanted by the user.
* Define a 4-place function `set_item` which has one extra argument `new_value` than the
    previous one. Return a version of the `Table` where the item in the
    designated address is changed to `new_value`. 
