**CS4341**

**Assignment \#2**

**Due: 2/3/17 @ 11:59 p.m.**

**The Problem**
===============

Your program will read in a list of integers in the range \[-9,9\]. The
length of the list will be divisible by 3. You must allocate those
numbers into 3 bins with the following restrictions:

1.  Each input value can only be assigned once. I.e., if there is only a
    single “1” in the input, you can only have a single “1” in one of
    the bins. If there are eleven instances of “1” in the input, you
    can place eleven 1s into whichever bins you like.

2.  Each bin must have an equal number of values.

Each of the three bins has different rules for scoring:

1.  Bin \#1: the scoring function is to alternately add and subtract the
    values in the bin.

2.  Bin \#2: for every pair of numbers at positions *i* and *i+1*, if
    the value at position i+1 is larger than position i, it scores +3.
    If the value at position i+1 is equal to the value at position i,
    it scores +5. If the value at position i+1 is smaller than at
    position i, it scores -10.

3.  Bin \#3: (positive) prime numbers in the first half of this bin
    score +4, all negatives values score -2, while composite positives
    score negative whatever their value is. For the second half of the
    bin, these values are inverted: primes scores -4, negatives score
    +2, and composite positives score whatever their value is. In the
    event of an odd number length, the value exactly in the middle is
    ignored.

Example input:

3 -2 5 -8 9 8 -4 5 0

If your program were to assign the values as follows:

Bin \#1: 8 -4 5

Bin \#2: 3 9 0

Bin \#3: -2 5 -8

Bin \#1 would score: +8 –(-4) + 5 = 17

Bin \#2 would score: 3&lt;9 scores +3, 9&gt;0 scores -10 for a total of
-7

Bin \#3 would score: -2 scores -2, 5 is ignored, -8 scores +2, for a
total of 0.

Total score: 17 + (-7) + 0 = 10

This example is illustrative. You should not assume there will be 9
input values. Your program should be able to handle 9999 numbers as
input.

Why did I pick such a twisted problem? It has several nice properties.
First, it is non-linear and non-trivial to optimize. Second, the
branching factor is rather high, so it provides an example of a problem
where generating all candidate next moves is not a good route forward.

**Approach**
============

You will create three approaches to solving this problem. For all of the
approaches, start with the numbers randomly assigned to the bins. Doing
so provides a natural starting point for hill climbing.

**First-choice hill climbing**
------------------------------

You will first implement first-choice hill climbing to solve this
problem. Your algorithm should allow no sideways moves. If it generates
100 successive candidate moves without finding one that improves the
situation, it should give up and treat its current state as a potential
solution. If time permits, you should restart the process with a new
random start state.

**Simulated annealing**
-----------------------

Extend your first-choice hill climbing code to make use of simulated
annealing. You will need to determine a temperature schedule, as well as
determine under what conditions to abort the search and perform a random
restart.

**Genetic algorithm**
---------------------

You will create a genetic algorithm to approach this problem. You must
make use of elitism, mutation, and experiment with population size.

**Analysis**
============

First, get your code working with a small test file to confirm you are
computing scores correctly, and are getting close to a global optimum.

Second, create a file called tune.txt. You will use this tuning data set
to determine the optimum value of parameters for your algorithms.

For simulated annealing, experiment with at least 3 different
temperature schedules and determine one that works well. Provide
performance data explaining why you chose the temperature schedule that
you did.

For genetic algorithms, experiment with at least 3 levels of elitism
(one of the amounts must be 0%). Similarly, experiment with 3 different
population sizes. The population sizes you experiment with should be
markedly different. Provide performance data for why you chose the
amount of elitism and the population size that you did.

Third, create a file called test.txt. You will use this testing file to
evaluate your design decisions in step 2. With this dataset, create a
performance graph for hill climbing, simulated annealing, and genetic
algorithms. You should run each of the optimization approaches with 0.1,
0.5, 1, 2, 5, 10, 30, and 60 seconds. Which algorithm does better? Does
the amount of time provides influence which is the best choice?

A key bit is that you use an **unseen** test file. When you optimize
your program’s settings to a particular file, in this case tune.txt, you
are doing something called *overfitting* to that dataset. We will
discuss overfitting in more detail when we get to machine learning. For
now, be sure you are happy with your settings for temperature,
population size, and elitism before running your final tests.

Your tune and test files should be large enough that your does not
quickly (&lt;5 seconds) reach asymptotic performance.

**Running your program**
========================

You should submit a program named *optimize* that takes three command
line arguments:

1\. The type of optimization to use: hill, annealing, ga

2\. The name of the input file containing the list of numbers

3\. The amount of time in seconds – can be floating point.

For example:

optimize annealing test1.txt 2.5

Should invoke your program using simulated annealing, read in and
optimize the values in test1.txt, and return an answer within 2.5
seconds.

You should also submit a toy test file you used to debug your code, and
a file named tune you used to determine ideal temperature schedules,
population size, etc. You should also submit a file named test that you
used to evaluate your program in the analysis section.

**Notes**
=========

1.  For stopping within the required time, if you go over by a small
    amount that is ok. You can implement the stopping criteria as if
    there is still time remaining, do another restart of the hill
    climbing algorithm. Hill climbing is typically fast, so if you go
    over by more than 0.1 seconds we’ll be grumpy.

2.  This assignment is much less specified than assignment \#1, and more
    details are left to your discretion and experimentation.

3.  More analysis is expected in this assignment.

4.  Part of your score will be based on the quality of the solutions
    your simulated annealing and genetic algorithm find to our test
    problems.


