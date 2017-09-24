# Description:

Unsupervised Discretization: Write code that takes a table column of N numbers, sorts in, and breaks into bins of size approximately sqrt(N). Note that these breaks have to satisfy the following sanity rules:

* no range contains too few numbers (sqrt(N));
* each range is different to the next one by some epsilon value (0.2 * standard deviation of that column);
* the span of the range (hi - lo) is greater than that epsilon;
* the lo value of one range is greater than than the hi value of the previous range


Supervised Discretization: Write code that reflects over the ranges found by the unsupervised discretizer. Combine ranges where some dependent variable is not changed across that combination of ranges. Specifically, sort the ranges and do a recursive descent of the ranges. At each level of the recursion, break the ranges at the point that most minimizes the expected value of the standard deviation of the dependent variable.

# How to run:
* Assuming that you have installed python 2.7, execute the command line as below in the terminal within the HW1 folder:

`python HW3.py`

## output

* For unsupervised descritization it prints the size of the ranges, span, the lowest value of the range, the highest value of the range.
* For the supervised descitization it prints the labels assigned to each range and the highest value of the range.

## Conclusion:

Supervised descritization produces fewer number of ranges.
