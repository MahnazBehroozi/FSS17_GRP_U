# HW2

## Description:

* Read lines from CSV files one a time incrementally updating column headers for each line.
* Headers are either Nums or Syms as determined by the magic characters in row1.
* Num and Syms incremental maintain knowledge about mean, standard deviation, and symbol counts in a column. 
* When the table reads row1, it builds the headers of Nums and Syms. And when the other rows are read, the headers get updated.

## Files:

* auto.csv : The input file that we have to run our code on it
* HW2.py: Python source code file for this assignment

## How to run:

* Assuming that you have installed python 2.7, execute the command line as below in the terminal within the HW1 folder:

`python HW2.py <file_name>`

## output

* It prints the header of the csv file following by the top 5 dominant rows and the bottom 5 dominant rows of the data based on the goal features 
