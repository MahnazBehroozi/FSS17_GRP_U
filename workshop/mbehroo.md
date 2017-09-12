# What we did in the workshop:

* we explored different Ks in KNN algorithm. The strategy I took for finding the best K is that to explore different Ks in ascending order and to find out how it helps the generalization of the algorithm. As we can see, k=1 makes the algorithm to overfit to the training examples. As we increase the k, it seems that it enhances the generalization of the algorithm. When K exceeds from some amounts, it again starts to gain low accuracies. So the best K layes some where between the extreme point of the spectrum. What helps us to choose the best K is to see how different amounts affects the accuracy of the testing samples classification.
So, I would say that I will choose a K between 30 to 50. (See png folder for visualized different tested Ks)

* We explored different kernel SVMs for training our model (rbf, polynomial, linear and sigmoid kernels). We also have been asked how to choose the best kernel. The answer is that it depends on the data we are working with. For example in the case of out workshop, linear kernel did the best and after that rbf was the best fit to our data and sigmoid was the worst of all.


