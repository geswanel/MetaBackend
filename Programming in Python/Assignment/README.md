# Assignments
Format
week: title
description, questions, some needed theory

## 1: Type casting input
Implicit and explicit casting difference and usage?

## 1: Module Quiz
Questions:
- What is static and dynamic typing in coding?
- how to use `input` function
- Explicit type casting to different types
- `isinstance` function
- break in loops? type of loops? `enumerate`
- How to delete a variable? What is happenning under python?
- Block indentation

## 2: Functions, Loops and Data structures
Menu ordering system that count the cost.
Creating functions, for loop to iterate collection, create and use data structures to store, retrieve, loop over data.

- What is the syntax to create a function?
    - What are scope types in python and what are difference between them?
    - How to use args and kwargs in python and what are difference?
- How does python float is built inside?

## 2: Read in data, store, manipulate and output new data to a file
Read a file in variety of ways. Write into file. Splitting strings

- How to open and close a file? What does open function return?
- Why do we need to use `with` statement?
- What are existing modes? How does `b` makes them different?
- How to read file and write into file?

## 2: Module Quiz
Questions:
- How does *args and **kwargs works in functions?
- What are common exceptions?
- How to open a file in different modes?
- What are built-in data structures? What are sequences and what aren't?

## 3: Mapping key-values to Dictionary data structures
Working with list and dict comprehensions, map and filter functions.
Working with data structures. Dictionaries
1. List of employee data => create usernames for login accounts
2. update the roster on the calendar, access to initials => dictionary

Questions:
- How to use map and filter function? How it operates and what are the differences?
- What are differences between comprehensions and map, filter functions?


## 3: Abstract Classes and Methods
Abstract class for a bank => specific bank
`abc` module `ABC`, `abstractmethod` - abstract base class
It turns out that it's possible to define overriden function with additional parameters. So the signature changes. [Read here about it](https://stackoverflow.com/questions/50008237/overriding-abstract-methods-in-python) - substitution principle violation.

There is no method overloading in python, so the last method definition will override the previous.

Questions:
- How to write abstract classes in Python?
- What are abstract classes and abstract methods?
- What are keywords to use?
- What is happening when a method or a function is overriden with another signature?
- What are SOLID principles in OOP?
- Inheritance types, Polymorphism and Encapsulation in python

## 3: Module Quiz
- Algorithm complexity calculation?
- How to make single, multi line comments? Doc comments
- What is a pure function?
- What are recursion advantages and disadvantages? Hanoi towers, factorial, fibonnachi

Additional questions to OOP:
- Static methods and variables in python?
- Class object, instance object. Class object fields, instance object fields. Self.


## 4: Import and Scope
Using import statements to import module and to import a particular function and a variable from a module.

Questions:
- How to parse json to python dict and vise versa?
    - json.loads(json_str) -> dict
    - json.dumps(py_dict) -> json_str (indent, separator)


## Question
What are AI and Machine learing? How are they different, connected?

## 4: Write a test
Write a test using PyTest
What are fixtures and how to use them?
How to run test using pytest?

Questions:
- What are test tools generally used in python?
- How to write basic tests with unittest built-in module?


## 4: Module Quiz
- How to make imports properly? What are common exceptions if import is not right?
- What are packages and libraries used in different domains of python programming?
- What is TDD? It's principles?
- What is pip used for? What is PyPI


## 5: Final Test
- int cannot cast float value string
- Iterating over different data structures using for loop?
- Complexity calculation
- issubclass function
- MRO