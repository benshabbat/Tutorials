# class Student:
#     def __init__(self, name: str,grades: list[int]):
#         self.name = name
#         self.grades = grades
#     def average_grade(self) -> float:
#         return sum(self.grades) / len(self.grades)
    
    
class Student:
    def __init__(self, name: str, grades: list[int]):
        self.name = name
        self.grades = grades

class GradeCalculator:
    def calculate_average(self, student: Student) -> float:
        return sum(student.grades) / len(student.grades)
    