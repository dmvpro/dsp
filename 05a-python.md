# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists and tuples are similar as they are both collections of data. But where they differ is that tuples are  heterogeneous data structures (i.e., their entries have different meanings), while lists are homogeneous sequences.  Since tuples are rigid and immutable, they qualify as ideal keys for dictionaries.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Python lists and sets are both collections of data but where they differ is that sets cannot contain duplicates and are unordered.  For example:  
`['alpha', 'beta', 'delta', 'gamma', 'alpha', 'beta'] # LIST: ordered, contains duplicates`  
`{'delta', 'alpha', 'gamma', 'beta'}                  # SET: unordered, no duplicates`  
>> Performance-wise, a hash lookup is used (which is why sets are unordered) to find an element in a set. This makes `__contains__` (in operator) a lot more efficient for finding elements in sets than lists.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Using `lambda` in Python allows a user to make a function that takes any number of arguments (including optional arguments) and returns the value of a single expression.  For example, setting `key = lambda` in a sorted function allows a user to sort by an alternate key of an object's indices:  
`>>> sorted(['Some', 'words', 'sort', 'differently'], key=lambda word: word.lower())`  
`['differently', 'Some', 'sort', 'words']`

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a tool for transforming one list into another list, usually by making a concise, single-line of code that could be written in a less efficient, less concise `for` clause.  For example:
```
doubled_odds = map(lambda n: n * 2, filter(lambda n: n % 2 == 1, numbers))  #use of map & filter
doubled_odds = [n * 2 for n in numbers if n % 2 == 1]                       #list comprehension
```
>> The capabilities of a list comprehension are very comparable, but the major difference is that list comprehension is more concise/easy-to-read and efficient than using map/filter with lambda. For set and dictionary comprehensions, it is a matter of using the proper formats for sets/dictionaries, for example:
```python
s = { x for x in range(10) }     # set comprehension occurs within curly brackets
L = ['a', 'b', 'c', 'd']         # set dictionary: 1st create a list of keys 
{letter: i for i,letter in enumerate(L, start=1)}   # then create a dictionary comprehension
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





