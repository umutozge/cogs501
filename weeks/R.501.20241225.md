COGS 501 - :calendar: 25/12 - Fall 2024
-----------------------------------------------

#### Reading
* No reading, just coding...

#### Checklist 
* Download the IMDB top-1000 [dataset](imdb_top_1000.tsv).
* Now the file is not a `csv` but a `tsv` (tab separated values). Therefore in
    reading the file you need to do the splitting not with `','` but with
    `'\t'`.
* Read this file and turn it into a `DataFrame`. A `DataFrame` is a dictionary
    with two keys: `columns`,`data`. The value of the `columns` field is the
    list of strings representing the column names (=first line in the file). The
    value of `data` is a list of lists. Each element list represents a row of
    the dataset. 
* Modify your representation of the `data` so that you have a list of
    dictionaries rather than a list of lists. Each dictionary will represent a
    row of the dataset. The keys of the row dictionary will be the column names
    and values will be the value of the corresponding column in that row.
* Define a function `wiew` that takes a data frame `df`, number of rows that
    defaults to 10 (`nrow=10`), a list of columns named `columns` that defaults
    to the full column list. and prints the data frame to the screen. 
* Define a function `dropc` (for "drop column") that takes a data frame `df` as
    first argument and a list of column names to drop, and returns a data frame
    exactly like `df` except the named columns are missing.
* Drop the `Poster_Link` column using `dropc`.
* Define a funcion `mapc` (for "map column") that takes 3 required arguments: `df` the
    data frame, `incol` the name of the column you want to map, `func` the
    function you want to use for mapping, and one optional argument `outcol` the
    name of the output column. If the `outcol` is provided, the newly created
    column will be added to the data frame under the given name. If `outcol` is
    not provided `incol` will be replaced by the new column. 
* Map the `Runtime` column to corresponding integer values (e.g. `124 min` to
    `124`).
* Use `mapc` to add a new column `TitleLength` that stores the number of words in the title of
    the movie.
* Define a function `focus` that takes a data frame `df` and a function `func`, which is a function that takes a row as an argument and retruns `True` or `False`. Your function `focus` will map `df` to another data frame where only the rows that return `True` for `func` are present.
* Use, for instance, `focus` to filter out the films earlier than a certain
    year, or those the product of rating and number of votes exceeds a certain
    limit, and so on. 

