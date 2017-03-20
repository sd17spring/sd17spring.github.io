---
title: Machine Learning
date: 2017-01-29 00:00:00 -05:00
description: ''
---

{% include toc %}

## Introduction

For this toolbox exercise you will learn how to teach your computer to learn!
Machine learning is a field that sits at the intersection of statistics, data
mining, and artificial intelligence.

Tom Mitchell defines what it means for a
computer program to learn in the following way:

> A computer program is said to
learn from experience E with respect to some class of tasks T and performance
measure P, if its performance at tasks in T, as measured by P, improves with
experience E.

This definition highlights a key difference between machine learning and
classical statistical methods. That is, machine learning is chiefly concerned
with improving future performance based on prior experience. Another key
difference with classical statistical methods is that machine learning focuses
on the computational efficiency (in both time and space) of algorithms. For
instance, an active area of machine learning research is to create algorithms
that have computational efficiency properties that work with “big data”.

This toolbox will familiarize you with doing basic supervised machine
learning. If you want more detailed reading on the subject, check out ["A few
useful things to know about machine
learning"](http://homes.cs.washington.edu/%7Epedrod/papers/cacm12.pdf).

## Get set

For this toolbox we will be learning how to do machine learning using the very
powerful [scikit-learn](http://scikit-learn.org/stable/) Python module. I
really like this library for several reasons:

1. It has a really clean API that lets you try many different machine learning algorithms with minimal changes to your code.
2. It has a lot of great built-in algorithms / techniques.
3. It automates the process of doing fair evaluations of a machine learning algorithm (this is the part that people often get wrong).

To install scikit-learn and related dependencies, execute the following
command:

    $ sudo pip3 install matplotlib scikit-learn scipy

Grab the starter code for this toolbox exercise via the normal fork-and-clone
method from <https://github.com//{{site.course.github_owner}}/ToolBox-MachineLearning>.

## Classification Using Scikit-Learn

There are many different problem settings in machine learning. One of the most
common is known as supervised classification. In the classification problem
setting, the goal is to categorize a piece of data into one of several
categories (or classes). This input data could be an image, a piece of text,
or an audio clip; basically anything that can be described numerically can
serve as the input to a classification algorithm. Here, we will investigate
supervised classification whereby the computer learns how to classify new
pieces of data by being shown a set of examples consisting of input data and
their corresponding category (or class).

To make things more concrete, let's look at one of the most well-studied
classification problems: recognizing images of [handwritten
digits](http://en.wikipedia.org/wiki/MNIST_database).

To load the digits and display 10 of the examples, run the `display_digits()`
function in the starter code.

The digit database built into scikit-learn has a total of 1797 examples (there
are many databases that are much bigger, the most famous is the [MNIST
database of handwritten digits](http://en.wikipedia.org/wiki/MNIST_database)).
Each digit is a grayscale 8x8 image. Our goal will be to train the computer to
categorize 8x8 grayscale images as being either a 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
by leveraging this database.

To get started, we will use a very simple classification algorithm called[
Multinomial Logistic
Regression](http://en.wikipedia.org/wiki/Multinomial_logistic_regression).
The basic idea will be to partition our data into two sets. The first set,
known as the training set, will be used to train our classifier (that is, we
will use it to infer the relationship between the appearance of an 8x8 patch
of pixels and the corresponding digit that it represents). The second set,
known as the testing set, will be used to evaluate our classifier on data that
it has not been trained on. The reason we need these two sets, is that
evaluating the performance of the classifier on the data it was trained on may
be misleadingly high (since the classifier may be overfitting to the
idiosyncracies of that training set). Here is some code for splitting the data
into two sets, training on one, testing on the other, and then reporting the
classification accuracy on the testing set.

``` python
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

data = load_digits()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target,
train_size=0.5)
model = LogisticRegression(C=10**-10)
model.fit(X_train, y_train)
print("Train accuracy %f" %model.score(X_train, y_train))
print("Test accuracy %f"%model.score(X_test, y_test))
```

## Learning Curves

Next, you will explore how the amount of training data influences the
performance of the learned model. In the previous example we used 50% of the
data for the training set and 50% for the testing set (we can see this since
we set `train_size = 0.5` when calling `train_test_split`). For this toolbox
you will be writing code to systematically vary the training set size versus
the testing set size and plot the curve of the resultant performance. You will
be repeating each value of `train_size` 10 times to smooth out variability. We
have given you starter code for this in the `train_model` function in
`machine_learning/learning_curve.py`.

Once you have produced this curve, answer the following questions and place
them in a text file called `questions.txt` in your `machine_learning` folder:

1. What is the general trend in the curve?
2. Are there parts of the curve that appear to be noisier than others? Why?
3. How many trials do you need to get a smooth curve?
4. Try different values for C (by changing `LogisticRegression(C=10** -10)`). What happens? If you want to know why this happens, see [this](http://en.wikipedia.org/wiki/Tikhonov_regularization) Wikipedia page as well as [the documentation](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) for `LogisticRegression` in **scikit-learn** .

## Turning in Your Toolbox Exercise

To turn in your toolbox, push your changes to `learning_curve.py` and your
writeup (`questions.txt`) to your GitHub repo and submit a pull request to
notify your friendly neighborhood NINJA to take a look.

## Further Explorations

If you want to explore more of the features of **scikit-learn**  and of machine
learning in general. I recommend you take a look at this [ipython
notebook](https://github.com/paulruvolo/DataScienceMaterials/tree/master/machine_learning_lecture_2).
If you are still interested, please contact the teaching team... we will be
happy to give more pointers.
