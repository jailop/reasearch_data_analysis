# KNN C++ implementation

![](knn.jpg)

This is a C++ implementation of the k-nearest neighbors algorithm for
classifition.

~~~~
Usage: ./evaluate [OPTIONS] dataset
  -e : Number of entities
  -a : Number of attributes
  -p : Proportion for train and test
  -s : Start for neighbors
  -f : Finish for neighbors
  -n : Normalize
       1 : Linear normatilization
       2 : Gaussian normailization
~~~~

Example:

    $ ./evaluate -e 150 -a 5 iris.csv
