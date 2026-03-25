Python Interview Questions - Extended Answers
============================================

**1. What is Python?**
Python is a high-level, interpreted, general-purpose programming language known for its readability and simple syntax. Widely used in web development, data science, automation, and more.

**2. What are Python’s main features?**
- Simple syntax similar to English
- Dynamically typed (no need to declare variable types)
- Interpreted → runs without compiling
- Object-oriented and supports functional programming
- Huge standard library and rich ecosystem

**3. What is PEP 8?**
PEP 8 is the official style guide for Python code. It defines best practices for formatting code for readability, such as indentation, naming conventions, and line length.

**4. What are Python’s data types?**
- Numbers: int, float, complex
- String: text data
- List: ordered, mutable sequences
- Tuple: ordered, immutable sequences
- Dict: key-value pairs
- Set: unique unordered elements
- Bool: True/False values

**5. Difference between list and tuple?**
- List: mutable (can change items), uses [ ]
- Tuple: immutable (cannot change items), uses ( )

**6. How to create a virtual environment?**
Use venv to isolate dependencies:

    python -m venv env

Activate it (Windows):
    env\Scripts\activate

macOS/Linux:
    source env/bin/activate

**7. What is the use of self in classes?**
self refers to the current object instance in class methods, letting you access attributes and methods of that instance.

**8. Difference between == and is?**
- == compares values
- is checks whether two variables reference the same object in memory

Example:
    x = [1, 2]
    y = [1, 2]
    x == y      # True
    x is y      # False

**9. What is a Python decorator?**
A function that modifies the behavior of another function or method. Often used for logging, validation, authentication, etc.

Example:
    def decorator(func):
        def wrapper():
            print("Before call")
            func()
            print("After call")
        return wrapper

**10. What is a lambda function?**
A small anonymous function defined using lambda. Useful for short, one-off functions.

Example:
    add = lambda x, y: x + y

**11. Explain list comprehension.**
A concise way to generate lists from iterables.

Instead of:
    squares = []
    for x in range(5):
        squares.append(x * x)

Use:
    squares = [x * x for x in range(5)]

**12. What is pickling?**
Converting Python objects to bytes for storage or transmission (serialization). Done via pickle module.

Example:
    import pickle
    data = pickle.dumps([1,2,3])

**13. Difference between append() and extend() in lists?**
- append() adds one item as a single element
- extend() adds multiple items from another iterable

Example:
    lst = [1,2]
    lst.append([3,4])    # [1,2,[3,4]]
    lst.extend([3,4])    # [1,2,3,4]

**14. How to handle exceptions in Python?**
Use try…except blocks to catch errors.

Example:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero.")

**15. What is __init__.py used for?**
Marks a folder as a Python package. Allows importing modules from that directory.

**16. What is the GIL?**
Global Interpreter Lock — prevents multiple native threads from executing Python bytecode at the same time in CPython. Affects multi-threaded performance.

**17. How to convert string to int?**
Use int():

    num = int("123")

**18. What does *args and **kwargs mean?**
- *args → variable number of positional arguments
- **kwargs → variable number of keyword arguments

Example:
    def func(*args, **kwargs):
        print(args, kwargs)

**19. Difference between shallow and deep copy?**
- Shallow copy → copies references of objects, not nested objects.
- Deep copy → copies all nested objects recursively.

Example:
    import copy
    deep_copy = copy.deepcopy(original)

**20. How to open a file in Python?**
Using a context manager:

    with open("file.txt", "r") as f:
        data = f.read()

**21. What is a module?**
A single Python file containing functions, classes, or variables that can be imported.

Example:
    import math
    print(math.sqrt(9))

**22. How to install packages in Python?**
Use pip:

    pip install requests

**23. What is list slicing?**
Extracting portions of a list.

Example:
    my_list = [0,1,2,3,4]
    print(my_list[1:4])  # [1,2,3]

**24. Explain generators.**
Functions that yield values one at a time instead of returning all data at once, saving memory.

Example:
    def gen():
        yield 1
        yield 2

**25. What are docstrings?**
Strings used as documentation for functions, classes, or modules. Accessed via help().

Example:
    def add(a, b):
        """Adds two numbers."""
        return a + b

**26. What is slicing syntax for reversing a list?**
Reverse a list quickly:

    reversed_list = my_list[::-1]

**27. What is a dictionary in Python?**
An unordered collection storing key-value pairs.

Example:
    my_dict = {"name": "Alice", "age": 30}

**28. Difference between remove() and pop() in lists?**
- remove(x) deletes first occurrence of value x
- pop(i) deletes and returns the item at index i

**29. How do you merge two dictionaries?**
Python 3.9+:

    merged = dict1 | dict2

Or:

    dict1.update(dict2)

**30. What is pass used for?**
A no-operation placeholder.

Example:
    def func():
        pass

**31. What is monkey patching?**
Changing or extending code behavior at runtime.

Example:
    import math
    math.sqrt = lambda x: "hacked!"

**32. What is a context manager?**
Manages resources like files or connections using with blocks to ensure proper cleanup.

Example:
    with open("file.txt") as f:
        data = f.read()

**33. Difference between @staticmethod and @classmethod?**
- @staticmethod → no access to class or instance
- @classmethod → receives class (cls) as the first parameter

**34. What is __name__ == "__main__" used for?**
Allows code to run only when the script is executed directly, not when imported as a module.

**35. How to get current working directory?**
Using os module:

    import os
    os.getcwd()

**36. What does zip() do?**
Pairs elements from multiple iterables.

Example:
    list(zip([1,2], [3,4]))  # [(1,3), (2,4)]

**37. How to create a set?**
A collection of unique, unordered elements.

Example:
    my_set = {1, 2, 3}

**38. What is enumerate()?**
Adds index counter to loops.

Example:
    for i, value in enumerate(["a", "b"]):
        print(i, value)

**39. Difference between break and continue?**
- break exits the loop entirely
- continue skips to next iteration

**40. What are f-strings?**
Formatted string literals introduced in Python 3.6.

Example:
    name = "Alice"
    print(f"Hello {name}")
