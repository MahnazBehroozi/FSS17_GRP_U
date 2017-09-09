# HW1

## Descriptions:

* Reads each line, kill whitepsace and anything after comment characters (#), break each line on comma, read rows into a list of lists (one   list per row), converting strings to numbers where appropriate. Note that some column headers contain ?: all such columns should be ignored. For now you can ignore the other magic characters in row1.

* Checks for bad lines (and bad lines will be skipped over); i.e. symbols where numbers should be and wrong number of cells (we will say that row1 has the “right” length).

* Reports runtimes loading datasets.

## Files:

* POM3A.txt : The input file that we have to run our code on it
* HW1.py: Python source code file for this assignment
* POM3A_noisy.txt: The test file with added noisy rows to test the ability of the code to ignore bad rows in the data
* diskFile.txt: The small data file for runing a mock example 
* POM3A_runtime.txt : Report of runtime loading and processing POM3A.txt file.

## How to run:
* Assuming that you have installed python 2.7, execute the command line as below in the terminal within the HW1 folder:

`python HW1.py <file_name>`
