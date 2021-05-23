## NOTE: REMOVE THE pass STATEMENTS WHEN COMPLETING THE FUNCTIONS! ##
from dataclasses import dataclass, asdict
from json import dumps
from typing import List, Dict, IO

@dataclass
class Student:
    """A student's course registration details"""
    given_name: str
    surname: str
    registered_courses: List[str]


def load_course_registrations(filename: str) -> List[Student]:
    """ Returns a list of Student objects read from filename"""
    with open('students.csv', 'r') as f:
        pass #TODO


def sort_by_courses_registered(students: List[Student]) -> List[Student]:
    """Sort students by the number of courses that they are registered for"""
    pass #TODO


def index_by_name(List[Student]) -> Dict[Tuple, Student]:
    """Store Students keyed by (surname, given_name) in a dictionary"""
    pass #TODO


def store_course_registrations(students: List[Student], filename:str):
    """Writes a list of Student to a file"""
    with open(filename, 'w') as f:
        pass #TODO
