

## Part B Analysis

Perform an analysis of the following recursive functions.

### function 1:

Analyze the following function with respect to number

```python
def function1(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		return value * function1(value, number-1)
```
Ans- 
when n >= 2, 5 + T(n-1)
i.e. T(n) = 5 + T(n-1)
t(n) will be evaluated as follows :- T(n-1) + T(n-2)...T(n-(n-2))+T(n-(n-1))+T(n-(n))
will be added till T(n-(n-2)) 
so T(n) = 5+ 5(n-2) +4
T(n) = 5n-1
y=mx+c form in which y becomes insignificant for higher values so we can remove -1,
 Also we can remove 5, since 0 <= n <= 6n ( 0 <= T(n) <= cf(n) ) for all n >= n'
so T(n) is 0(n)

### function 2:

Analyze function2 with respect to the length of the mystring.  Hint, you will need to set up two mathematical functions for operator counting.  one for function2 and the other for recursive_function2

```python

def recursive_function2(mystring,a, b):
	if(a >= b ):
		return True
	else:
		if(mystring[a] != mystring[b]):
			return False
		else:
			return recursive_function2(mystring,a+1,b-1)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)

```
Ans- 

 function2 is simply returning the result of recursive_function2 so order of growth will be the same. So, we can calculate the order of growth of recursive_function2, the return value and '-' operator in the return value of function2 will consitute +2 in T(n) but being constants, it will be a correct practice to ignore them.

Let mystring be the input/parameter to function2
Let n = len(mystring)
Order of growth of function2 = order of growth of recursive_function2

Let T(n) = total number of operations required to generate a return value of recursive_function2
T(n) = 5 + T(n-3)

When n = 3, true is returned by recursive_function2, lets say T(0) = 1, since true = 1, false = 0
T(n) = 5 + 5(n/3) + T(0)
T(n) = 5 + 5(n/3) + 1
Therefore, T(n) is O(n)
Hence, function2 has order of growth of it's run-time as O(n)


### function 3 (optional challenge):

Analyze the following function with respect to number

```python
def function3(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		half = number // 2
		result = function3(value, half)
		if (number % 2 == 0):
			return result * result
		else:
			return value * result * result

```


## Part C Reflection

1. Describe how to a approach writing recursive functions, what steps do you take?
Ans- the correct approach in making a recursive function is by making base case must be setup that would terminate the process of recursive calling. And whether base case is reached needs to be checked.Also for optimizing the function the time and space complexity should also be calculated.

2. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same? 
In recursive analysis, it is important to consider how the function is broken down into smaller inputs and how the recurrence relation is applied and whether the base case is reached terminating the recursive function. they are similar in a way because in both the analysis we ignore the constants




## Submitting your lab

In order to get a mark for this lab, you must submit:

- a complete working solution for every function in part A.

Also, please make sure you follow the steps listed below for a full mark:

- Place the analysis part for this lab into the file lab3.md

When you are happy with the state of your files, submit a link to your repo's lab3 folder into blackboard.  

Note: Submission of a link to Blackboard is an indication that your lab is ready for grading in the current state.  Do not submit a link until you are ready to be graded.



## Lab Rubric:

| Criteria       | Poor - 0 mark     | Fair - 0.5 marks                                                                                                                     | Good - 1 marks                                                              |
| -------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| Lab Completion | Part A not completed | Coding Completed, analysis/reflection is missing or poorly done | Successfully complete coding, analysis and reflection portions |
