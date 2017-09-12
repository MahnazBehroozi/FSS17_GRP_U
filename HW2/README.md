# HW2

## Description:

* Read lines from CSV files one a time incrementally updating column headers for each line.
* Headers are either Nums or Syms as determined by the magic characters in row1.
* Num and Syms incremental maintain knowledge about mean, standard deviation, and symbol counts in a column. 
* When the table reads row1, it builds the headers of Nums and Syms. And when the other rows are read, the headers get updated.
* *Dominate function has not been added yet*

## Files:

* auto.txt : The input file that we have to run our code on it
* HW2.py: Python source code file for this assignment

## How to run:

* Assuming that you have installed python 2.7, execute the command line as below in the terminal within the HW1 folder:

`python HW1.py <file_name>`

## output

* Uncomment lines 177 and 183 to see an example of how the code gives reports on mean and the mode for num and sym variables respectively. 
