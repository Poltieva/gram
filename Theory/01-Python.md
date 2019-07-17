# <center> **Back to Basics** </center>
## <center> **Volume 1** </center>

### **Why Python?**

Python is a great language, especially for beginners, which is proved by the fact that it's now the most popular introductory language at American colleges. Python is designed to be easy to program and easy to read. It has so little excess code that it seems like it's written in plain English. If you understand English, you already understand Python.

### **What Python looks like?**

Python uses indentation to give structure to the code. People who are used to other languages often complain about the absence of braces, but this is one of the key advantages of Python! In languages that use braces, people also use indentation to make it more readable for other people. Thus, they use braces to tell the program what they mean and indentation to tell other people what they mean. In Python, there is just one way to denote structure in a way that is easy for both humans and computers to read - indentation. There is just one thing to watch out for: never mix tabs and spaces.

### **Variables**

To create a variable and assign a value of a certain type to it, use `=`:

Integer:    `x = 3`  
Float:      `x = 3.3`  
Boolean:    `x = True`  
String:     `x = "Hello world!"`  
List:       `x = ["Hello", "world", "!"]`  
Tuple:       `x = ("Hello", "world", "!")`  
Set:         `x = {"Hello", "world", "!"}`  
Dictionary:  `x = {"Hello": True, "world": True, "!": True}`

To check the type of the value assigned to the variable, use `type(var)`:


```python
x = ["Hello", "world", "!"]
print(x)
print(type(x))
```
> ['Hello', 'world', '!']
>
> <class 'list'>

```python
x = True
print(type(x))
```
> <class 'bool'>


### **Simple Arithmetics**

There is nothing special about numeric operations in Python. Write them in the same way that you were taught at school:

```python
1 + 5 * 2 - 3 / 3 + 6 % 5
```
> 11.0


`%` returns the remainder.

You can use `+` and `*` for strings and lists, too:

```python
print("Hello " + "world!")
```
> Hello world!

```python
print("Hello " * 3)
```
> Hello Hello Hello 


```python
print(['Monty', 'Python'] + ['and', 'the', 'Holy', 'Grail'])
```
> ['Monty', 'Python', 'and', 'the', 'Holy', 'Grail']


### **Numerical Comparison Operators**

Numerical comparison operators can be applied to any type of data. The result of such operation is of type Boolean, which means that the operation will return either `True` or `False`.

`<`   less than  
`<=`  less than or equal to  
`==`  equal to (don't confuse with the assignment operator `=`)  
`!=`  not equal to  
`>`   greater than  
`>=`  greater than or equal to


```python
print(3 > 4)
```
>False


```python
print(["hello"] == ["hello"])
print("hello" == "hello")
```
> True
>
> True


When applied to strings, the comparison operators check the letters of the strings one by one and consider the letters that go higher in the alphabet:

```python
print("hello" > "yell")
```
>False

```python
print("hello" > "bell")
```
>True


### **String Processing**

The following useful methods are checks that return either `True` or `False`:

`s.startswith(t)`   test if `s` starts with `t`  
`s.endswith(t)`     test if `s` ends with `t`  
`t in s`            test if `t` is a substring of `s`  
`s.islower()`       test if all letters that `s` contains are lowercase  
`s.isupper()`       test if all letters that `s` contains are uppercase  
`s.istitle()`       test if all words in `s` have initial capitals  
`s.isalpha()`       test if `s` is non-empty and contains only letters  
`s.isalnum()`       test if `s` is non-empty and contains only letters and digits  
`s.isdigit()`       test if `s` is non-empty and contains only digits  


```python
print("Monty Python".istitle())
```
>True

```python
print("MONTY PYTHON".isupper())
```
>True

```python
print("MONTY PYTHON".isalpha())
```
>False

```python
print("Monty Python".endswith("Python"))
```
> True

By the way, you can use `and`, `or` and `not` to combine different expressions that are of type **Boolean**.

```python
my_string = "MontyPython"
print(my_string.isalpha() and "on" in my_string and my_string != "Python")
```
>True

The methods and functions below return either numbers or strings (by the way, methods are the ones with the period after the variable):

`len(s)`           return the length of `s`  
`s.count(t)`       return the number of `t` in `s`  
`s.lower()`        return the lowercased string `s`  
`s.upper()`        return the uppercased string `s`  
`s.title()`        return the string `s` with every word capitalized  
`s.strip()`        remove the spaces at the beginning and at the end of the string `s`  
`s.replace(t, u)`  replace every `t` with `u` in the string `s`

For example:
```python
my_string = "___Monty python"
print(len(my_string))
print(my_string.upper())
print(my_string.count("on"))
print(my_string.strip("_"))
```
> 15
>
> ___MONTY PYTHON
>
>2
>
>Monty python


You can mix and match, too: 
```python
print(my_string.strip("_").title().replace("on", "ON"))
```
>MONty PythON


Indexing and slicing of strings in Python is quite natural:

`s.find(t)`        return the index of `t` in `s`, otherwise `-1`  
`s.rfind(t)`       return the index of `t` in `s` looking from the end of the string, otherwise `-1`  
`s[n]`             returns the `n`th character of `s`  
`s[beg:end]`       returns a substring of `s` from `beg` till `end` (excluding the `end`th character)  
`s[:end]`          returns a substring of `s` from the beginning of `s` till `end` (excluding the `end`th character)  
`s[beg:]`          returns a substring of `s` from `beg` till the end of `s`

For example:


```python
my_string = "Monty Python"
print(my_string[6])
print(my_string[6:])
print(my_string[:5])
print(my_string.find("on"))
print(my_string.rfind("on"))
```
>P
>
>Python
>
>Monty
>
>1
>
> 10

Negative indices can also be used. They are counted starting from the end of the string, i.e. `-1` is the index of the last element of the string.

For example:
```python
my_string = "Monty Python"
print(my_string[-4:-1])
```
>tho



```python
my_string = "Monty Python"
print(my_string[-1] == my_string[len(my_string) - 1])
```
>True

There is no built in reverse function for strings, but we can use the [extended slice](http://docs.python.org/2/whatsnew/2.3.html#extended-slices) syntax. It works by doing `[begin:end:step]` - by leaving begin and end off and specifying a step of -1, it reverses a string.

Also, you can extract the elements of a string that have even indexes:

```python
my_string = "Monty Python"
print(my_string[::2])
```
>MnyPto

```python
my_string = "Monty Python"
print(my_string[::-1])
```
>nohtyP ytnoM


#### **Formatting**

Let us take an easy start by looking into **formatting strings**. Once in a while you will need to print something in a pretty way. You can use the `format` method to do that. Use curly brackets to show where the values of the variables should be placed. For example:

```python
"{} has loved {} since he was {}.".format("Derek", "Monty Python", 12)
```
>'Derek has loved Monty Python since he was 12.'

You can use numbers to define the order of variables:


```python
"from {1} to {0}".format("Z", "A")
```
>'from A to Z'

You can also define the number of characters allocated for the variable value with `:n` and the alignment with `<` and `>`.

```python
"{:10}".format(911)
```
>   '       911'

```python
"{:<10}".format(911)
```
>   '911       '

You can read more about the `format` usage [here](https://mkaz.com/2012/10/10/python-string-format/).

### **List Processing**

There also exist a lot of useful methods and functions for list processing:

`len(m)`           return the length of the list `m`  
`m.index(t)`       return the index of `t` in the list `m`  
`m.count(t)`       return the number of `t`s in `m`  
`sorted(m)`        return the sorted list `m`  
`reversed(m)`      return the reversed list `m`  
`s in m`           test if `s` is an element of `m`

For example:

```python
my_list = ["Hello", "world", "!"]
print(my_list.index("!"))
print(my_list.count("!"))
print(sorted(my_list).index("!"))
```
>2
>
>1
>
>0

These methods modify the existing list:
`m.sort()`         sort the list `m`  
`m.reverse()`      reverse the list `m`  
`m.append(t)`      add `t` element to the end of the list `m`  
`m.insert(i,t)`    add `t` element to the `i` index position of the list `m`  
`m.extend(t)`      iterate over `t` and add each element to the list `m`  
`m.remove(t)`      remove the first occurrence of `t` in the list `m`  
`m.pop()`          remove and return the last element of the list `m`

For example:
```python
my_list = ["Hello", "world", "!"]
print(sorted(my_list))

my_list.sort()
print(my_list)
```
>['!', 'Hello', 'world']
>
>   ['!', 'Hello', 'world']

```python
my_list = ["Hello", "world", "!"]
print(my_list.pop())
print(my_list)
```
>!
>
>   ['Hello', 'world']

`append` adds its argument as a single element to the end of a list. The length of the list itself will increase by one.

```python
my_list.append("?")
print(my_list)
print(len(my_list))
```
>['Hello', 'world', '?']
>
>   3

```python
my_list.append(["?","?"])
print(my_list)
print(len(my_list))
```
>['Hello', 'world', '?', ['?', '?']]
>
>   4

`extend` iterates over its argument adding each element to the list, extending the list. The length of the list will increase by the number of elements that occurred in the iterable argument.


```python
my_list.extend(["?","?"])
print(my_list)
print(len(my_list))
```
>    ['Hello', 'world', '?', ['?', '?'], '?', '?']
>
>    6

Basically, the following three snippets are semantically equivalent:

1)
```python
for item in iterator:
    a_list.append(item)
```
2)
```python
a_list.extend(item)
```
3)
```python
a_list += item

#or

a_list = a_list + item
```

Indexing and slicing of lists is natural, too:

`m[n]`             returns the `n`th element of `m`  
`m[beg:end]`       returns a sublist of `m` from `beg` till `end` (excluding the `end`th element)  
`m[:end]`          returns a sublist of `m` from the beginning of `s` till `end` (excluding the `end`th element)  
`m[beg:]`          returns a sublist of `m` from `beg` till the end of `s`

You can also change a separate element of a list in Python:

```python
my_list = ["Monty", "python"]
print(my_list[1])
my_list[1] = my_list[1].title()
my_list
```
>['Monty', 'Python']

The `max()` method returns the largest element in an iterable.  
The `min()` method returns the smallest element in an iterable.
```python
my_list = [18, 19, 21, 22]
print('The smallest number from my_list is:', min(my_list))
print('The largest number from my_list is:', max(my_list))
```
>The smallest number from my_list is: 18
>
>The largest number from my_list is: 22

The `sum()` function adds the items of an iterable and returns the sum.

```python
numbers = [20, 3, 14, -5]
numbersSum = sum(numbers)
print(numbersSum)
```
>32

### **Tuples**

The major difference between tuples and lists is that tuples can not be changed. In technical terms, tuples are **immutable**. In practical terms, they have no methods that would allow you to change them.

A tuple is defined in the same way as a list, except that the whole set of elements is enclosed in parentheses instead of square brackets.

```python
a_tuple = ("Monty", "python", 1, 2, 3)
a_tuple
```
>('Monty', 'python', 1, 2, 3)

The elements of a tuple have a defined order, just like a list. Tuple indices are zero-based, just like a list, so the first element of a non-empty tuple is always a_tuple[0].


```python
a_tuple[0]
```
>'Monty'

Negative indices count from the end of the tuple, just like a list.

```python
a_tuple[-1]
```
>3

Slicing works too, just like a list. When you slice a list, you get a new list; when you slice a tuple, you get a new tuple.

```python
a_tuple[1:3]
```
>('python', 1)

Tuples do not over-allocate. Since a tuple's size is fixed, it can be stored more compactly than lists which need to over-allocate to make `append()` operations efficient.

This gives tuples a nice space advantage:
```python
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("A is of type", type(a), "and has the length of", len(a))
print("B is of type", type(b), "and has the length of", len(b))
print('A =', a.__sizeof__(), "bytes")
print('B =', b.__sizeof__(), "bytes")
```
> A is of type <class 'tuple'> and has the length of 10
>
> B is of type <class 'list'> and has the length of 10
>
> A = 104 bytes
>
> B = 120 bytes


**But remember!**  "Premature optimization is the root of all evil".

### **Dictionaries**

The dictionary is another useful data type built into Python. Unlike strings and lists, which are indexed by a range of numbers, dictionaries are indexed by keys. A key can be a string or a number.

A dictionary in Python looks like a pair of curly braces containing a comma-separated list of `key:value` pairs: `{key1:val1, key2:val2, key3:val3}`.

How to work with dictionaries:

`d[key] = val`    store `val` in `d` under `key`  
`d[key]`          return the value associated with `d` (look it up)  
`d.keys()`        the list of keys in `d`  
`d.values()`      the list of values in `d`  
`sorted(d)`       the keys of `d`, sorted  
`key in d`        test whether a particular `key` is in the dictionary `d`  
`d1.update(d2)`   add all items from `d2` to `d1`  
`del d(key)`      remove the key with the assigned value from `d`

See an example below:

```python
synonyms = {"rain":["shower", "downpour", "drizzle"],
            "snowfall":["snow", "blizzard"]}
synonyms["wind"] = ["breeze", "gust"]
synonyms
```
> {'rain': ['shower', 'downpour', 'drizzle'], 'snowfall': ['snow', 'blizzard'], 'wind': ['breeze', 'gust']}

```python
synonyms.keys()
```
> dict_keys(['rain', 'snowfall', 'wind'])

```python
synonyms.values()
```
>dict_values([['shower', 'downpour', 'drizzle'], ['snow','blizzard'], ['breeze', 'gust']])

```python
for i in synonyms.keys():
    print("The best synonym for {} is {}.".format(i, synonyms[i][0]))
```
> The best synonym for rain is shower.
>
> The best synonym for snowfall is snow.
>
> The best synonym for wind is breeze.

**NB!** The keys are unique, which means that, if you store a value using a key that is already in use, the old value associated with that key is forgotten. If you are trying to extract a value using a non-existent key, Python will raise an error.

```python
synonyms["wind"]
```
>['breeze', 'gust']

```python
synonyms["wind"].append("gale")
synonyms["wind"]
```
>['breeze', 'gust', 'gale']

```python
synonyms["sun"]
```
> KeyError    
>
> \<ipython-input-492-96989a7d2973\> in \<module\>()
>
>    ----> 1 synonyms["sun"]
>
>    KeyError: 'sun'

An updated version of dictionaries is the `defaultdict` type from the `collections` library. It's very useful. You can inspect it on your own using [the examples here](https://www.accelebrate.com/blog/using-defaultdict-python/).

### **Dictionaries vs Lists**

Assume we have a list of stop words we want to filter from a text:

```python
import time
start = time.time()

stopwords = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 
            'for', 'from', 'has', 'he', 'in', 'is', 'it', 'its',
            'of', 'on', 'that', 'the', 'to', 'was', 'were',
            'will', 'with']
# Do it many times to test performance.
for i in range(1000000):
    filtered = []
    for w in ['Mr.', 'Hat', 'is', 'feeding', 'the', 'black', 'cat', '.']:
        if w not in stopwords:
            filtered.append(w)

end = time.time()
print("Time:", end - start)
```
>Time: 5.764584064483643


Let's convert stopwords to **dictionary** type.

```python
import time
start = time.time()

stopwords = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 
            'for', 'from', 'has', 'he', 'in', 'is', 'it', 'its',
            'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will', 'with']

stopwords = dict.fromkeys(stopwords, True)
# Do it many times to test performance.
for i in range(1000000):
    filtered = []
    for w in ['Mr.', 'Hat', 'is', 'feeding', 'the', 'black', 'cat', '.']:
        if w not in stopwords:
            filtered.append(w)

end = time.time()
print("Time:", end - start)
```
>Time: 1.6147301197052002

```python
print(stopwords)
```
>{'a': True, 'an': True, 'and': True, 'are': True, 'as': True, 'at': True, 'be': True, 'by': True, 'for': True, 'from': True, 'has': True, 'he': True, 'in': True, 'is': True, 'it': True, 'its': True, 'of': True, 'on': True, 'that': True, 'the': True, 'to': True, 'was': True, 'were': True, 'will': True, 'with': True}

The `dict.fromkeys()` method takes a list of keys + a default value for all keys, and returns a new dictionary. Using this approach the algorithm takes around second to run.

Python dictionaries use hash tables, this means that a lookup operation (e.g., if x in y) is **O(1)**. A lookup operation in a list means that the entire list needs to be iterated, resulting in **O(n)** for a list of length n.

### **Sets**

A set in Python represents an unordered collection of unique elements. You can check the length of a set (`len(s)`), sort it (`sorted(s)`), iterate across the set (`for i in s:`) and check whether the set includes an element (`x in s`). Sets do not support indexing or slicing, so better use lists if you need those.

Why use sets then? Let us look at an example. What if you need to count the number of unique words in the text? A set can help you with that. See how it works:

```python
text = "How much wood could a woodchuck chuck if a woodchuck " + \
       "could chuck wood ?"
text = text.lower().split()
print(text)
```
>['how', 'much', 'wood', 'could', 'a', 'woodchuck', 'chuck', 'if', 'a', 'woodchuck', 'could', 'chuck', 'wood', '?']

```python
len(text)
```
>14

```python
x = set()
print(type(x))
```
><class 'set'>

```python
set(text)
```
> {'?', 'a', 'chuck', 'could', 'how', 'if', 'much', 'wood', 'woodchuck'}

```python
len(set(text)) * 100.0 / len(text)
```
> 64.28571428571429

The percentage of distinct words in `text` var is ~ 64%:

Methods that can be performed on sets:

`s.issubset(t)`            test whether every element in `s` is in `t`  
`s.issuperset(t)`          test whether every element in `t` is in `s`  
`s.union(t)`               return a new set with elements from both `s` and `t` (`s OR t`)  
`s.intersection(t)`        return a new set with elements common to `s` and `t` (`s AND t`)  
`s.difference(t)`          return a new set with elements in `s` but not in `t` (`s AND (NOT t)`)  
`s.symmetric_difference(t)` return a new set with elements in either `s` or `t`, but not both

Sets are created using curly brackets.


```python
prn_subj = {"I", "you", "he", "she", "it", "we", "they"}
prn_obj = {"me", "you", "him", "her", "it", "us", "them"}
prn_subj.intersection(prn_obj)
```
>{'it', 'you'}

```python
prn_subj.difference(prn_obj)
```
> {'I', 'he', 'she', 'they', 'we'}

```python
prn_subj.symmetric_difference(prn_obj)
```
>{'I', 'he', 'her', 'him', 'me', 'she', 'them', 'they', 'us', 'we'}

```python
prn_subj.union(prn_obj)
```
>{'I', 'he', 'her', 'him', 'it', 'me', 'she', 'them', 'they', 'us', 'we', 'you'}

Another way to join two sets is:
```python
prn_subj | prn_obj
```
>{'I', 'he', 'her', 'him', 'it', 'me', 'she', 'them', 'they', 'us', 'we', 'you'}

Some other useful methods:

`s.add(x)`        add `x` to `s`  
`s.remove(x)`     remove `x` from `s`; raises `KeyError` if not present  
`s.discard(x)`    remove `x` from `s` if present  
`s.pop()`         remove and return an arbitrary element from `s`; raises `KeyError` if empty  
`s.clear()`       remove all elements from `s`

```python
prn_subj = {"I", "you", "he", "she", "it", "we", "they"}
prn_subj.add("New value")
print(prn_subj)
```
>{'he', 'you', 'we', 'I', 'it', 'New value', 'they', 'she'}

```python
prn_subj.remove("we")
print(prn_subj)
```
>{'he', 'you', 'I', 'it', 'New value', 'they', 'she'}


### **Moving from Type to Type**

The most popular transformations in text processing are `split()` and `join()`:

`s.split()`        split `s` into a list of strings using whitespaces as a separator  
`s.split(sep)`     split `s` into a list of strings using `sep` as a separator  
`sep.join(m)`      join all elements of `m` using `sep` as a separator  
`int(s)`           transform `s` into a integer  
`float(s)`         transform `s` into a float  
`str(n)`           transform `n` into a string  
`set(l)`           transform `l` into a set  
`tuple(d)`         transform `d` into a tuple  
`list(s)`           transform `s` into a list  

For example:

```python
my_string = "Monty Python"
print(my_string.split())
```
>['Monty', 'Python']

```python
print(my_string.split("on"))
```
>['M', 'ty Pyth', '']

```python
my_list = ['Monty', 'Python']
print(" ".join(my_list))
```
> Monty Python

If your code contains a mistake, Python tells you the line containing the mistake and what the mistake is. For example, in the following code we are trying to concatenate a string with a number:

```python
num = 5
print("The number of cakes that Liza can eat is " + num)
```
> \<ipython-input-511-8c7774b85913\> in \<module\>()
>
>1 num = 5
>----> 2 print("The number of cakes that Liza can eat is " + num)
>  
>TypeError: must be str, not int

```python
num = 5
print("The number of cakes that Liza can eat is " + str(num))
```
> The number of cakes that Liza can eat is 5

Converting one sequence to another:

```python
print(set([1,2,3,3,3,2]))
print(tuple({5,6,7}))
print(list('hello'))
print('hello'.split())
```
>{1, 2, 3}
>
> (5, 6, 7)
>
> ['h', 'e', 'l', 'l', 'o']
>
> ['hello']

To convert to dictionary, each element must be a pair:

```python
dict([[1,[2,2]],[3,4]])
```
> {1: [2, 2], 3: 4}

### **Conditions**

In order to write a conditional expression, use `if condition: do this`. If you need more than one check, use `elif condition: do this`. An `else: do that` expression works as a default condition. For example:

```python
my_string = "Python"
if my_string.islower():
    print(my_string, 'is a lowercase word.')
elif my_string.istitle():
    print(my_string, 'is a titlecase word.')
else:
    print(my_string, 'is something else.')
```
> Python is a titlecase word.


**NB!** Pay attention to indentation in conditions.

### **Iterable and Iterator**

Iterable is a “sequence” of data, you can iterate over using a loop. The easiest visible example of iterable can be a list of integers – `[1, 2, 3, 4, 5, 6, 7]`. However, it’s possible to iterate over other types of data like strings, dicts, tuples, sets, etc.

Iterator protocol is implemented whenever you iterate over a sequence of data. For example, when you use a for loop the following is happening on a background:

* first `iter()` method is called on the object to converts it to an iterator object.
* `next()` method is called on the iterator object to get the next element of the sequence.
* `StopIteration` exception is raised when there are no elements left to call.


```python
simple_list = [1, 2, 3]
my_iterator = iter(simple_list)
print(my_iterator)
```
> <list_iterator object at 0x10844e0b8>

```python
next(my_iterator)
```
> 1

### **Loops**

In order to perform the same action(s) a couple of times or on each element of the string or list, use a loop. 

The most basic type of loop in Python is the **while** loop, which keeps repeating as long as the conditional statement evaluates to True:

```python
i = 0
while i < 5:
    print(i)
    i = i + 1
```
>0
>
>1
>
>2
>
>3
>
>4


`for i in s: do this` iterate over each character of a string or each element of a list  
`for i in range(num): do this` perform the same action `num` times  
`i` is just a local variable that works as an iterator.

Let us nest the condition from the previous section into a loop:

```python
my_list = ["Hello", "world", "!"]
for word in my_list:
    print("Word:", word)
    if word.islower():
        print(word, 'is a lowercase word.\n')
    elif word.istitle():
        print(word, 'is a titlecase word.\n')
    else:
        print(word, 'is something else.\n')
```
>Word: Hello
>
>Hello is a titlecase word.
>
> Word: world
>
>world is a lowercase word.
>
> Word: !
>
> ! is something else.

Here is an example with `range()`:

```python
for i in range(4):
    if i == 2:
        print("Happy birthday, dear Liza!")
    else:
        print("Happy birthday to you!")
```
>Happy birthday to you!
>
>Happy birthday to you!
>
>Happy birthday, dear Liza!
>
>Happy birthday to you!


### **List Comprehensions**

List comprehensions provide a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.

The list comprehension always returns a result list.

The basic syntax is `[ expression for item in list if conditional ]`

This is equivalent to:
```python
for item in list:
    if conditional:
        expression
```
Example:

```python
import time
start = time.time()

result = []
for i in range(10000000):
    result.append(i)

end = time.time()
print(end - start)
```
>2.0825510025024414


You can obtain the same thing using list comprehension even faster:

```python
import time
start = time.time()

result = [i for i in range(10000000)]

end = time.time()
print(end - start)
```
> 0.875105619430542


Also, we can use if conditions with list comprehension:


```python
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([i for i in a if i > 5])
```
>[8, 13, 21, 34, 55, 89]


### **Generator Expressions**

Generators are iterators, but you can only iterate over them once. It’s because they do not store all the values in memory, they generate the values on the fly.

When you call a normal function with a return statement the function is terminated whenever it encounters a return statement. In a function with a `yield` statement the state of the function is “saved” from the last call and can be picked up the next time you call a generator function.

Generators allow us to ask for values as and when we need them, making our applications more memory efficient and perfect for infinite streams of data. 

**Note**: Keep in mind that generator expressions are drastically faster when the size of your data is larger than the available memory.


```python
def my_gen():
    for x in range(5):
        yield x
        
val = my_gen()
```


```python
next(val)
```
> 0

Generator expression allows creating a generator on a fly without a yield keyword. However, it doesn’t share the whole power of generator created with a yield function. The syntax and concept is similar to list comprehensions:


```python
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
print(gen_exp)
```
><generator object <genexpr> at 0x1353522b0>



```python
for x in gen_exp:
    print(x)
```
> 0
>
> 4
>
> 16
>
> 36
>
> 64

In terms of syntax, the only difference is that you use parentheses instead of square brackets. However, the type of data returned by list comprehensions and generator expressions differs.

```python
list_comp = [x ** 2 for x in range(10) if x % 2 == 0]
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
print(list_comp)
print(gen_exp)
```
>[0, 4, 16, 36, 64]
>
><generator object <genexpr> at 0x135352990>


The main advantage of generator over a list is that it takes much less memory. We can check how much memory is taken by both types using `sys.getsizeof()` method.


```python
from sys import getsizeof
my_comp = [x * 5 for x in range(1000)]
my_gen = (x * 5 for x in range(1000))
print(getsizeof(my_comp))
print(getsizeof(my_gen))
```
>9024
>
>88

We can see this difference because while `list` creating Python reserves memory for the whole list and calculates it on the spot. In case of generator, we receive only ”algorithm”/ “instructions” how to calculate that Python stores. And each time we call for generator, it will only “generate” the next element of the sequence on demand according to “instructions”.

On the other hand, generator will be slower, as every time the element of sequence is calculated and yielded, function context/state has to be saved to be picked up next time for generating next value. That “saving and loading function context/state” takes time.

### **Functions**

To define a function, use `def name(arguments): do this`. Every function should have a documentation line that states what the function does. The documentation line is enclosed in triple quotation marks. For example:

```python
def check_words(my_list):
    """Check every word in my_list."""
    for word in my_list:
        if word.islower():
            print(word, 'is a lowercase word.')
        elif word.istitle():
            print(word, 'is a titlecase word.')
        else:
            print(word, 'is something else.')
```

**NB!** Pay attention to indentation in functions.

Here is an example of calling a function:

```python
check_words(["Hello", "world", "!"])
```
>Hello is a titlecase word.
>
>world is a lowercase word.
>
>! is something else.

If you need a function to return a value, use `return`. There is a big difference between `return` and `print`. `print` just prints anything you need to be printed; `return` returns the value and terminates the function. For example:

```python
def fraction_of_words(aList, word):
    """Check the fraction of word in aList."""
    return aList.count(word) * 100 / len(aList)
    print("hi there")
    

my_list = ["hello", "monty", "python", "hello", "!"]
print(fraction_of_words(my_list, "hello"))
```
> 40.0


The `print` expression is not performed here because it is stated after the `return` expression.

### **Comments**

If you need to add a comment to your program, put `#` at the beginning of the comment:

```python
def check_words(aList):
    """Check every word in aList."""
    # this is a comment
    for word in aList:           # and this is a comment, too
        if word.islower():
            print(word, 'is a lowercase word.')
        elif word.istitle():
            print(word, 'is a titlecase word.')
        else:
            print(word, 'is something else.')
```

### **Working with Files**

When opening a file, you should state whether you open it for reading or writing. 

`open("address", "r")`       open a file for reading  
`open("address", "w")`       open a file for writing  
`open("address", "a")`       open a file for adding

Methods for reading a file and writing to a file:

`f.read()`           read a file as a string  
`f.readlines()`      read a file as a list of strings (lines in the file)  
`f.write()`          write a string to a file

`With`-statement is a nice way to work with files. Just make sure that the indentation is correct. The following piece of code reads the `problems.txt` file from the current directory and prints it line by line. The method `.strip()` is used here for removing the new line characters `\n`.

With the "With" statement, you get better syntax and exceptions handling. 

In addition, it will automatically close the file. The with statement provides a way for ensuring that a clean-up is always used.



```python
with open("data/problems.txt", "r") as f:
    for line in f:
        print(line.strip())
```
> Multiply 13456 by 6 , and that 's it .
>
> Subtract 1 from 16 , and that 's it .
>
> What if you subtract 19 from 1200 ?
>
> ...

Without the "With" statement, we would write something like this:

```python
f = open("data/problems.txt", "r")
for line in f:
        print(line.strip())

# It's important to close the file when you're done with it
f.close()  
```
> Multiply 13456 by 6 , and that 's it .
>
> Subtract 1 from 16 , and that 's it .
>
> What if you subtract 19 from 1200 ?
>
> ...

Read from one file, process and write to a different file. Here, every first word from each line in the `problems.txt` is written to `new_file.txt`.

```python
with open("data/problems.txt", "r") as f:
    with open("data/new_file.txt", "w") as out_f:
        for line in f:
            line = line.strip()
            words = line.split(' ')
            out_f.write(words[0] + '\n')
```

```python
with open("data/new_file.txt", "r") as f:
    for line in f:
        print(line.strip())
```
> Multiply
>
>Subtract
>
>What
>
>Try
>
>What
>
>...


### **Working With Directories**

This is where we start to `import` things. It's often necessary to check or change the directory you are working in or to process all files in some directory. The `os` (Miscellaneous operating system interfaces) library contains the necessary tools. To use the library, you will have to import it first: `import os`. Here are some useful functions:

`os.getcwd()`                            return the current directory  
`os.chdir("/address/to/a/directory/")`   change the current directory  
`os.listdir("/address/to/a/directory/")` return the list of files in the directory  
`os.listdir(".")`                        return the list of files in the current directory  
`os.path.isfile("path")`                 return True if path is an existing regular file

To read more about `os` library click [here](https://docs.python.org/3/library/os.html).

For example:


```python
import os
r = os.getcwd() + "/data/"
print(r)
for item in os.listdir(r):
    if not item.startswith('.') and os.path.isfile(os.path.join(r, item)):
        print(item)
```
>/Users/vitalik/CompLing-Summer-School/lectures/data/
>
>new_file.txt
>
>jekyll_hyde.txt
>
>declaration_for_kids.txt
>
>is_valid_password.py
>
>jekyll_hyde_tokenized.txt
>
>...


In this way, you can open and process each file in the directory.

```python
for item in os.listdir(r):
    if not item.startswith('.') and os.path.isfile(os.path.join(r, item)):
        with open(os.path.join(r, item), "r") as f:
            print(f.readline())
```

    Multiply
    
    Mr. Utterson the lawyer was a man of a rugged countenance that was never lighted by a smile; cold, scanty and embarrassed in discourse; backward in sentiment; lean, long, dusty, dreary and yet somehow lovable.
    ......

    


### **Python Classes and Objects**

Classes are used to create new user-defined data structures that contain arbitrary information about something.

For example, let’s say you wanted to track a number of different animals. If you used a list, the first element could be the animal’s name while the second element could represent its age.

How would you know which element is supposed to be which? What if you had 100 different animals? Are you certain each animal has both a name and an age, and so forth? What if you wanted to add other properties to these animals? This lacks organization, and it’s the exact need for classes.

We can think of class as a prototype (sketch) of a house. It contains all the details about the floors, doors, windows etc. Based on these descriptions we build the house. The house is the object.

```python
class Shark:
    "This is my class"
    a = 10
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")

print(Shark.a)
print(Shark.swim)
print(Shark.be_awesome)
print(Shark.__doc__)
```
>10
>
>\<function Shark.swim at 0x1040afd08\>
>
>\<function Shark.be_awesome at 0x1040af7b8\>
>
>This is my class

An object is an instance of a class. We can take the Shark class defined above, and use it to create an object or instance of it.

```python
sammy = Shark("Sammy")
stevie = Shark("Stevie")
```

```python
sammy.be_awesome()
stevie.swim()
```
>Sammy is being awesome.
>
>Stevie is swimming.

Compare this:
```python
class Student(object):
    def __init__(self, name, age, gender, level, grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}

    def setGrade(self, course, grade):
        self.grades[course] = grade

    def getGrade(self, course):
        return self.grades[course]

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)

# Define some students
john = Student("John", 12, "male", 6, {"math":3.3})
jane = Student("Jane", 12, "female", 6, {"math":3.5})

# Now we can get to the grades easily
print(john.getGPA())
print(jane.getGPA())
```
>3.3
>
>3.5


with a standard Dict:
```python
def calculateGPA(gradeDict):
    return sum(gradeDict.values())/len(gradeDict)

students = {}
# We can set the keys to variables so we might minimize typos
name, age, gender, level, grades = "name", "age", "gender", "level", "grades"
john, jane = "john", "jane"
math = "math"
students[john] = {}
students[john][age] = 12
students[john][gender] = "male"
students[john][level] = 6
students[john][grades] = {math:3.3}

students[jane] = {}
students[jane][age] = 12
students[jane][gender] = "female"
students[jane][level] = 6
students[jane][grades] = {math:3.5}

# At this point, we need to remember who the students are and where the grades are stored.
# Not a huge deal, but avoided by OOP.
print(calculateGPA(students[john][grades]))
print(calculateGPA(students[jane][grades]))
```
>3.3
>
>3.5


### **Modules**

A collection of variable, function definitions and classes in a file is called a Python **module**. A collection of related modules is called a **package**.

What if you want to save some functions in a file and have access to it from any other place? This can be easily done using `import`.

Suppose you save the function `is_palindrome(word)` in a module named `word_checks.py`. To use this function in a different module, you should import it:

```python
    >>> from word_checks import is_palindrome
    >>> is_palindrome("racecar")
    True
```

To import all functions from a module, use `import` and the name of the module, but then you will have to add the name of the module when calling a function from it:

```python
    >>> import word_checks
    >>> word_checks.is_palindrome("racecar")
    True
```

**NB!** To import functions from a file and use them in REPL, you should change your current working directory to the one that contains the file with functions as described in the section above. To import functions from one file and use them in another file, place the files in the same directory. All this does not apply to the standard libraries.

If you are interested in the ways to import modules from other directories, see https://docs.python.org/3.6/tutorial/modules.html.

### **Bibliography**

1. Python 3.6 documentation, available at https://docs.python.org/3/
2. Python String Format Cookbook, available at https://mkaz.com/2012/10/10/python-string-format/
3. Using defaultdict in Python, available at https://www.accelebrate.com/blog/using-defaultdict-python/
4. Natural Language Processing with Python, available at http://www.nltk.org/book/
5. Learning Python by Mark Lutz, available at http://www.amazon.com/Learning-Python-Edition-Mark-Lutz/dp/1449355730
