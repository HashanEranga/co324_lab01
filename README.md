# CO324 Lab 1: Python data structures and I/O
## Objective
Review some basic concepts of  Python programming including input-output, data structures, OOP and lambdas.

## Preparation
Install Python version 3.7 or newer on your computer. You may use whichever IDE or editor that you prefer.

## Instructions
* Use only the standard built-in modules in Python to complete these exercises.
* Put the solutions to coding exercises in file `lab01.py`.
* **DO NOT** change any code in `lab01_test.py`.
* Solutions to short answer questions should be in a single plain text file named answers.txt.

## References
* [Python data classes](https://realpython.com/python-data-classes)
* [JSON in Python](https://realpython.com/python-json)

## Exercises
### Q1
Each of the file `student_registrations.csv` contains the following student details: first and last names, followed by a list of courses that they have completed separated by commas.

```python
from dataclasses import dataclass
from typing import List, Dict, IO

@dataclass
class Student:
    """A student's course registration details"""
    given_name: str
    surname: str
    registered_courses: List[str]

# Example object:
s1 = Student("Saman","Silva",["CO324","CO321","CO325"])
```
 Read the file into a list of `Student` objects by completing this function.
```python
def load_course_registrations(file: str) -> List[Student]:
    """ Returns a list of Student objects read from filename"""
```

### Q2
We can use the built-in `sorted` function to sort the list by surname and given name.
```python
sorted(student_list, key = lambda s: s.surname + s.given_name)
```

Complete the following function to sort students by the number of courses that they are registered for in *descending* order (Hint: apply the `len` function.)
```python
def sort_by_courses_registered(List[Student]) -> List[Student]:
```

### Q3
Complete the `load_course_registrations` that stores Student objects in a dictionary using a tuple (surname, given_name) as the key.
```python
def load_course_registrations(filename: str) -> List[Student]:
    """ Returns a list of Student objects read from filename"""
```

### Q4
JSON is a common format for exchanging data between web APIs. We can serialise our Student class as JSON as follows.
```python
from dataclasses import asdict
from json import dumps

s1 = Student("Saman","Silva",["CO324","CO321","CO325"])
dumps(asdict(s1))
```

Use Python's `map` function to apply `dataclass.asdict` to a list of Student objects. Then use `json.dump` to write the output to a  given file name.
 ```python
def store_course_registrations(List[Student], filename:str):
 ```
