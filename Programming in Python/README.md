## Prestudy

- Python Basics
    - comments, variables, loops, conditions, functions, error exceptions
- Programming paradigms
    - procedural, functional, object oriented
- Libraries and modules
- AI
- testing, TDD

## Time
5w 6-9 hours = 30-45 h (44 h on the certificate page)
5h video + 12h reading = 17 h material
12 graded + Labs


## 1 WEEK: Introduction
### Introduction to course
- Intro: curriculum
- How python used?
    - tensorflow
    - backend
    - classify mri data

### Introduction to programming
- Intro
    - Distributed computing, Cloud computing, AI
    - Binary and Transistors
    - Programming - giving set of instructions to the computer
- Why Python
    - Web, AI, ML, Data analytics
    - Easier to learn and work with -> speed to market.
    - 1991
    - English + Math
- Running code
    - python shell
    - cmd
    - IDE
- Python syntax
    - separating instructions
        - indentation and spaces; semicolon to separate instructions `print(1); print(2);`; backslash to continue in new line
    - commenting `#`
    - variables
        - naming conventions `myName` camelCase, `my_name` snake_case
        - ***`del` keyword in python*** to delete a variable
    - basic dt `type` function
        - Numeric: Integer, Float, Complex
        - Sequences: String, List, Tuples
            - Strings
                - Unicode encoding
                - `len` function
                - indices, `+`, multi-line`\`, single-line
        - Dictionary: Dict `key: value`
        - Boolean: `True` `False`
        - Set
    - Comparison operators
    - Build in functions
        - `print` `input` `len`
    - creating functions with and with out parameters
- type casting
    - implicit - int -> float
    - explicit: `str` `int` `float` `ord` `hex` `oct` `bin` `list` `set` `dict`
- user input, console output
    - `input()` - prompt can be passed. Always return str => typecasting for other types
    - `print()`
        - `"{0} {1}".format(a, b)`, `"{}, {}".format(a, b)`
        - arithmetic
        - `sep`, `end`, `object`
- Additional resources
    - [Python built-in functions](https://docs.python.org/3/library/functions.html)
    - [W3Schools](https://www.w3schools.com/python/default.asp)
    - [Practice skills](https://www.hackerrank.com/domains/python)

### Control flow and conditionals
- math, logical operators
    - `+ - * /`
    - `and, or, not`
- flow control
    - conditional: if - elif - else
    - switch `match`: `| = or` and `_` - default
    - loops: for, while
        - sequences, `range`, `enumerate`
        - flow charts
        - `break`, `continue`, `path`
        - nested loops and time complexity
            - `time` module - `time.time()` function

### Module Summary
- programming history
- python benefits
- running IDE and running code
- python syntax
    - spaces and indentation
    - commenting
    - variables and datatypes
    - typecasting
    - flow control (conditionals, loops, nested loops)
- Additional resources
    - [Control flow](https://docs.python.org/3/tutorial/controlflow.html)
    - [Conditional operators](https://www.w3schools.in/what-is-conditional-operator)
    - [Conditional statements](https://realpython.com/python-conditional-statements/)


## 2 WEEK: Basic programming
### Functions and DS
- Function - piece of code that can be used repeatedly
    - `round` `print` `input`
    - args and kwargs
        - passing any number of positional (tuple) or keyword arguments (dictionary)
- Variable scope: LEGB
    - Local - inside the function. Not accessible in GB
    - Enclosing - outside a nested function but inside parent function
    - Global - outside any function
    - Built-In - `print`, `input` and other functions and variables
- Data structures
    - User-Defined: Tree, Queue, Stack, HashMap, Graph, LinkedList
    - Built-In: Lists, Tuples, Sets, Dictionaries
        - Lists - 0 ind dynamic array that stores any datatype `l = [1, 2, 3, "world"]` (`l[ind]` to read or modify element)
            - add element: `index(id, val)`, `append(val)`, `extend(iterable)`
            - del element: `del ar[ind]`, `ar.pop(ind)`
            - iterate using for loop, unpacking for print function
        - Tuples - immutable lists `tup = (1, 2, "hello")`
            - `count`, `index(val)`
        - Sets - not a sequence. Stores unique values `{1, 2, 3}`
            - `.add(val)` `.remove(val)` `.discard(val)`
            - set theory operations: `.union = |`; `.intersection = &`; `.difference = -`; `.symmetric_difference = ^`
        - Dictionaries - **Key:Value** pairs. Keys are unique
            - `d[key]` - reading and modifying
            - `del d[key]` - deleting key
            - standard iterating by key. `items` to return key, value pair
    - Mutable and Immutable
- Choosing and using data structures
- Additional resources
    - [Python datastructures](https://docs.python.org/3/tutorial/datastructures.html)
    - [datastructures](https://realpython.com/python-data-structures)

### Error, exceptions and files handling
- Errors
    - Syntax - indentation, colon; mispelling in the program
    - Exceptions - runtime (code execution);
- Exception handling
    - `try` - for block of code that throws exception
    - `except` - to catch exception
        - `except exceptiontype as e`
        - chain except
        - Examples: `IndexError`, `Exception`, `ZeroDivisionError`, `FileNotFoundError`
- File handling
    - `open(filepath, mode)`
        - modes: `r`(default), `w`, `r+`, `a`
            - binary: `rb`, `wb`, `rb+`, `a`
        - **`w` creates a file**
    - read functions `read(num of char or full text if blank), readline(same), readlines()`
        - iterating through file objects same as `readlines`
    - write functions `write, writelines`
    - `close`
    - `with open() as f` statement closes automatically
- Path
    - Absolute
    - relative
- Exercise
    - `split`
    - `random.choice`

### Module Summary
- Functions and DS
    - creating function, scopes, kwargs, args,
    - Data structures: List, Tuple, dict, Set
- Files and error handling
    - try except
    - open, close, read, write
- Additional resources
    - [Exception and Errors](https://docs.python.org/3/library/exceptions.html)
    - [File handling](https://pynative.com/python/file-handling/)

## 3 WEEK: Programming paradigms
### Procedural
- Procedural programming
- Algorithms and complexity

### Functional programming
- Pure function
- Recursion
- Reversing a string
- map, filter
- comprehensions

### OOP
- Intro
- Principles
- Classes and instances
- instantiate
- instance methods
- parent class vs child class
- Inheritance, multiple inheritance
- Abstract classes and methods
- MRO

## 4 WEEK: Modules, Packages, libraries and tools
### Modules
- What is a module?
- Accessing modules
- import
- namespacing and scoping
- reload

### Packages, Libraries, Frameworks
- Numpy, Pands, Matplotlib
- Data analysis packages
- ML packages: Pytorch, TensorFlow
- Web frameworks

### Testing tools
- What is testing
- types of testing
- test automation packages
- Pytest
- TDD