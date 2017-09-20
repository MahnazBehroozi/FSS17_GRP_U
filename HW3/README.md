# Description:

Write code that takes a table column of N numbers, sorts in, and breaks into bins of size approximately sqrt(N). Note that these breaks have to satisfy the following sanity rules:

* no range contains too few numbers (sqrt(N));
* each range is different to the next one by some epsilon value (0.2 * standard deviation of that column);
* the span of the range (hi - lo) is greater than that epsilon;
* the lo value of one range is greater than than the hi value of the previous range
