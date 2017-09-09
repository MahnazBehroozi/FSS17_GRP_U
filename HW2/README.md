# HW2

## Description:

* Read lines from CSV files one a time incrementally updating column headers for each line.
* Headers are either Nums or Syms as determined by the magic characters in row1.
* Num and Syms incremental maintain knowledge about mean, standard deviation, and symbol counts in a column. 
* When the table reads row1, it builds the headers of Nums and Syms. And when the other rows are read, the headers get updated.
