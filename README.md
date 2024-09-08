# Python-exercise
ML Programming Assignment 2: Numpy
Please follow the instructions to complete the following Python
programs. For each program, please also provide your own
testing cases. Please complete them in either Jupter notebook
or with .py file and submit your programs and running results.
1 The open prices of SP500 between January 2, 2018 to January 16, 2018 are listed as following:
2683.72998,2697.850098,2719.310059,2731.330078,2742.669922,2751.
149902,2745.550049,2752.969971,2770.179932,2798.959961
and the close prices of SP500 between January 2, 2018 to January 16, 2018 are listed as
following:
2695.810059,2713.060059,2723.98999,2743.149902,2747.709961,2751.
290039,2748.22998,2767.560059,2786.23999,2776.419922
Write a Python program to assign the open prices and the close prices to two Numpy arrays,
calculate the daily earnings during that period of time and output them. Then calculate the mean
and the standard deviation of the daily earnings for SP500 between January 2, 2018 to January
16, 2018, and output the mean and the standard deviation. Display the daily earnings as one
standard deviation of the mean, two standard deviations of the mean, three standard deviations of
the mean, etc.
2 Let’s place the open prices and close prices of SP500 between January 2, 2018 to January 16,
2018 which are listed in problem 1 in a Cartesian coordinate system, where the open prices are
represented as x-coordinates and close prices are represented as y-coordinates. Write a Python
program to store them in a Numpy array. The program then finds the two points which together
form the two diagonal corners of a rectangle such that the rectangle has the largest area. The
program next finds the two points which together form the two diagonal corners of a rectangle
such that the rectangle has the largest perimeter.


===========================================================================
Python Excercise-ML1
 
# using random.sample()
# to generate random number list
res = random.sample(range(1, 5000), 1000)
print ("Random number list is : " +  str(res))
===========================================================================
Key points for efficient handling of large lists:
Use functional programming constructs like map, filter, and reduce for concise and efficient operations.
Leverage lambda functions for anonymous functions, reducing boilerplate code.
Consider using generator expressions for memory-efficient iteration over large datasets.
If performance is critical, explore libraries like NumPy for optimized array operations.
By following these guidelines, you can effectively solve these problems with large lists of numbers using functional programming in Python.
==============================================
 
Write code with using a profiler to execute a high-performance code.
Profile the code using any methods but profile memory and CPU
==============================================
1.	Sum of Squares:
Calculate the sum of the squares of all numbers in the list.
2.	Product of Cubes:
Compute the product of the cubes of all numbers in the list.
3.	Average of Even Numbers:
Find the average of all even numbers in the list.
4.	Maximum Odd Number:
Determine the maximum odd number present in the list.
5.	Minimum Even Number:
Find the minimum even number present in the list.
6.	Count Positive Numbers:
Count the number of positive numbers in the list.
7.	Count Negative Numbers:
Count the number of negative numbers in the list.
8.	Frequency of a Number:
Given a target number, count the number of times it appears in the list.
9.	Factorial of Each Number:
Compute the factorial of each number in the list.
10.	Square Root of Each Number:
Calculate the square root of each number in the list.
11.	Filter Numbers Divisible by 3:
Create a new list containing only the numbers divisible by 3 from the original list.
=================================================================
 
12.	Filter Numbers Greater Than 5:
Create a new list containing only the numbers greater than 5 from the original list.
13.	Map Numbers to Their Squares:
Create a new list where each element is the square of the corresponding element in the original list.
14.	Map Numbers to Their Cubes:
Create a new list where each element is the cube of the corresponding element in the original list.
15.	Reduce to the Sum of Squares:
Use the reduce function to calculate the sum of the squares of all numbers in the list.
===================================================================
Information about profiling:
Profiling Efficiently
The first aim of profiling is to test a representative system to identify what’s slow (or using too much RAM or causing too much disk I/O or network I/O). Profiling typically adds an overhead (10× to 100× slowdowns can be typical), and you still want your code to be used in as like a real-world situation as possible. Extract a test case and isolate the piece of the system that you need to test. Preferably, it’ll have been written to be in its own set of modules already.
The basic techniques that are introduced first in this chapter include the %timeit magic in IPython, time.time(), and a timing decorator. You can use these techniques to understand the behavior of statements and functions.
Then we will cover cProfile (“Using the cProfile Module”Links to an external site.), showing you how to use this built-in tool to understand which functions in your code take the longest to run. This will give you a high-level view of the problem so you can direct your attention to the critical functions.
Next, we’ll look at line_profiler (“Using line_profiler for Line-by-Line Measurements”Links to an external site.), which will profile your chosen functions on a line-by-line basis. The result will include a count of the number of times each line is called and the percentage of time spent on each line. This is exactly the information you need to understand what’s running slowly and why.
Armed with the results of line_profiler, you’ll have the information you need to move on to using a compiler ([Link to Come]).
In [Link to Come], you’ll learn how to use perf stat to understand the number of instructions that are ultimately executed on a CPU and how efficiently the CPU’s caches are utilized. This allows for advanced-level tuning of matrix operations. You should take a look at [Link to Come] when you’re done with this chapter.
After line_profiler, if you’re working with long-running systems, then you’ll be interested in py-spy to peek into already-running Python processes.
To help you understand why your RAM usage is high, we’ll show you memory_profiler (“Using memory_profiler to Diagnose Memory Usage”Links to an external site.). It is particularly useful for tracking RAM usage over time on a labeled chart, so you can explain to colleagues why certain functions use more RAM than expected.
If you’d like to combine CPU and RAM profiling you’ll want to read about Scalene (“Combining CPU and Memory Profiling with Scalene”Links to an external site.), this combines the jobs of line_profiler and memory_profiler with a novel low-impact memory allocator and also contains experimental GPU profiling support.
VizTracer (“VizTracer for an interactive time-based call stack”Links to an external site.) will let you see a time-based view on your code’s execution, it presents a call stack down the page with time running from left-to-right. You can click into the call stack and even annotate custom messages and behaviour.

