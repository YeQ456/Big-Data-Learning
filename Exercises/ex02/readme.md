Spark RDD
Lab assignment: Exercises with MapReduce on Apache Spark
The aim of this notebook is to play with the RDD API of Apache Spark, aiming to solve the same four MapReduce exercises we did for the first lab.
Note that in the previous lab, we solved the exercises at a conceptual level, tackling most exercises with a single Map followed by a single Reduce function. In Spark, we may be able to concatenate multiple map (or flatMap) functions to transform the input data into what we want, letting Spark optimize the whole job, which is going to be easier (and more efficient) to implement. Moreover, we will have a lot more functions available apart from Map and Reduce.
