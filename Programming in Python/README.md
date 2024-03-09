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
- programming model or paradigm - structure of code
- DRY principle
### Procedural
- Procedural programming
    - subroutines = functional sections of code
    - hard to maintain, extend. No relation with real world objects, Data is exposed
    - Reusable code, easy to understand and learn
- Algorithms and complexity
    - sequence of steps to solve a problem. 
    - Recursion, D&Q, DP, Greedy
    - Complexity: O(1), O(n), O(logn), O(n^2), O(nlogn), O(2^n), O(n!)
        - accessing element, linear search, binary search, bubble sort
        - identify input, loops, combine complexity of nested, dominant term, simplify
- Additional Resources
    - [programming styles in python](https://newrelic.com/blog/nerd-life/python-programming-styles)
    - [types of algorithms in python](https://www.thetechplatform.com/post/different-types-of-algorithms-in-data-structure)
    - [Big-O](https://dev.to/sarah_chima/the-big-o-notation-an-introduction-34f7)

### Functional programming
- Functional programming
    - Clean, consistence, maintability
    - **First class citizen**
        - can be assigned, passed, returned
    - Function takes input and produces output
    - |             |Traditional   | Pure|
      |-------------|--------------|-----|
      |R/U global   |Yes           | No  |
      |Modify local | Yes          | Yes |
      |Change args  | Yes           | No |
      |input dependent| No         | Yes |
    - `map` `sorted` `slices`
    - doesn't change data outside function
- Pure function - doesn't change outside data
    - Consistency, Cache (predetermined outcome), Multithreading (no effect on global)
    - No access and modify global scope
- Recursion - repetitive itself call
    - Neat, Seq generation, complex task segmentation
    - Memory, hard to follow and debug
    - Factorial example
    - Hanoi Towers example
- Reversing a string
    - slices [a:b:c]
        - a, b ommition meaning (as far)
- map, filter
    - map - applies passed function to every element and return results
    - filter - applies passed function to every element and return element with True results
    - map and filter objects
- comprehensions
    - list, dict, set, generator comprehensions
    - `[<f(val)> for <geting val> if <cond>]`
    - `zip` creates list of tuples from lists => for dict comrehensions with 2 lists
- `join`
- Additional resources
    - [map, reduce, comprehensions](https://www.knowledgehut.com/blog/programming/python-map-list-comprehension)
    - [recursion](https://realpython.com/python-recursion/)
    - [Functional programming](https://stackabuse.com/functional-programming-in-python/)


### OOP
- Paradigm - style of writing code. Reduces complexity and defines development flow.
    - OOP - reusability, simplicity, modularity, easier to understand, abstraction
        - Classes - blueprint of an object. Define attributes(variables) and behavior(methods = class functions)
        - Objects - instance of a class. Instanciation
        - Methods - behavior of a class
        - Main concepts
            - Inheritance - creating a new class derived from other class (child - parent)
                - MRO - rules that python uses to order of functions and variables implemented in classes. Also determines a scope
            - Polymorphism - different behavior of a function for different objects with same interface (`+` `*` for numbers and strings). Many forms.
            - Encapsulation - secure data from unwanted modification. (hiding data and functionality)
                - public - can be accessed everywhere
                - protected - `self._a` - can be accessed within the class and its subclasses
                - private - `self.__b` - can be accessed within the class
                    - name mangling `_class__identifier`
                    - public functions to access private/protected data'
                - Not strict access control
            - Abstraction - hide important information or unnecessary implementation
                - `abc` module `ABC` class (Abstract Base Class)
        - Other concepts: Method overriding, overloading, constructors etc.
    - Procedural, Functional, EventDP, FlowDP, Logic, Declarative 
- Classes and instances
    - Class - combine variables(attributes) and behaviors(methods)
    - class object - instantiation and attribute reference
    - instance object - attribute reference and method reference with `self`
    - method object
    - Instantiation process: Define a class, Declare an instance, Initialize an instance
    - How to create a class and instantiate from it? How to access attribute and method using class or instance object?
    - Attribute reference should be done via class or instance objects.
- Define a class example
    - passing `self` in the method declares that it's the method of **instance**
    - There can be **class** and **instance** attributes
    - changing instance attribute doesn't affect class attribute
        - however when instance attribute is default - **class attribute modification affects instances**
    - `docstring`
    - `pass` keyword - means continue execution witout impacting functionality flow
- Instantiation - Reusability - different instances -> different outcomes, same class
    - `__new__` creats an object
    - `__init__` constructor - takes object created by `new` and initializes it
- Instance methods and variables
    - State of instance objects = values of instance variables (attributes)
    - instance methods can help to change instance object state without affecting other instances
- Parent class vs Child class
    - Inheritance helps to pass variables and functionality from parent/base to child/sub class (Reusability)
    - `super()` method to access a parent class
    - changing child instance variables doesn't affect parent.
    - `object` - default base class
- Inheritance, multiple inheritance
    - Multiple inheritance separated by comma
    - Multi-level inheritance - last class wins (attribute **mro**)
    - Built-in functions - `issubclass(child, parent)`, `isinstance(instance, class)`
    - `super()` - gives access to parent class and siblings
    - `dir` function returns all properties and methods of the passed object
- Exercises 
    - Statements inside class executed irrespective of the instance creation.
    - Scope of variables inside class namespace
    - by default printing object returns address
- Abstract classes and methods
    - hide implementation, interoperability, consistency, avoiding duplication
    - `abc` module `ABC` class and `@abstractmethod` decorator
        - **decorator** - helper function that changes behavior of passed function
    - Can't instantiate from it
    - Subclasses must override every abstract method - ensure functionality of derived classes
    - Implementing abstract classes
        - methods implemented in derived class
        - `super` function
- MRO - Method Resolution Order - provides rules to identify the order in which methods and attributes are passed through in search of the hierarchy of classes for resolution
    - Linearization order of a class
    - Inheritance types: Simple, Multiple, Multilevel, Hierarchical, Hybrid
    - MRO identifies methods and attributes from bottom to top, from left to right
        - DFS
        - C3 linearization algorithm
            - Monotonicity
            - Super class visited only after local classes
    - `obj.mro()` method and `help(obj)` function
    - MRO is Python’s way of resolving the order of precedence of classes while dealing with inheritance.

### Module Summary
- Paradigms
    - Procedural
        - Algorithm
        - Complexity
        - Big-O
    - Functional
        - Pure Function
        - Recursion
    - OOP
        - 4 main concepts: Inheritance, Polymorphism, Encapsulation, Abstraction
        - Class, instance, method object
        - Instantiation, changing state

- `super` function usage?
- [Additional resources](https://www.coursera.org/learn/programming-in-python/supplement/zHCMs/additional-resources)


## 4 WEEK: Modules, Packages, libraries and tools
### Modules
- What is a module? - building block of code that can be imported to add functionality
    - Consist of statement and definitions
    - Breaking down code functionality into managable parts
    - Advantages
        - Reusability
        - Scope (module namespace)
        - Simplicity - reduce interdependency - specific purpose
    - `import` modules imported once. Code inside is executed
        - typically imported at the beginning. But can be imported in the function or at any other place.
    - Built-in modules (`math`)
    - `matplotlib`
    - Accessing
        - Any python file can be a module
        - Current-directory -> Built-In -> pythonpath -> Installation dependent default dir
        - `sys.path()`
        - `calendar.leapdays(), calendar.isleapyear()`
    - `import` statement
        - current file = `main` module
        - importing files from the current directory
        - importing built-in modules - python std library (`math` `random` etc)
        - importing modules from folder in the current directory (`sys.path.insert`)
            - Why do I need to use `sys.path` if i can just use `import folder.module`?
        - Python Package Index. PyPI (cmd:`pip install numpy`) => `import numpy`
        - Examples
            - `import math` import module - used as `math.sqrt`
            - `from math import sqrt` `from math import sqrt, log10` `from math import *` - importing functions, classes and variables from module file
                - no imported object in the scope of main file
                - using `*` - bad practice because it's confusing where a certain function came from and it may lead to coflicts between module functions.
            - `import math as m`, `from math import factorial as f` - aliases for module and module objects
    - Namespacing and Scoping
        - Namespace - Mapping from names to objects. Similar to `dict` data structure for mapping
            - module = namespace
        - Scope - place in a python programm where namespace are accessible
        - Scope types LEGB - scope resolution rule
            - Local
            - Enclosed - `nonlocal` keyword to access variables from the parent function within the nested one
            - Global - `global` keyword to access global variables within a function
            - Built-in
        - `id` function to get address
        - variables are local by default
            - local to module or local to function
    - `reload` function in `importlib` module
        - module load once but reload can help to load it more times
        - to dynamically change code and information
        - `os.listdir()` example with dynamic changes

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


### Additional information
- `__pycache__` - bytecode files to facilitate project running. Safe to delete.
- `super` usage