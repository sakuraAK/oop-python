# Aggregation

class Student:
    def __init__(self, name):
        self.__name = name
    
    def __str__(self):
        return f"Student name: {self.__name}"
    

class Course:
    def __init__(self, name, hrs):
        self.__name = name 
        self.__hrs = hrs
        self.__list_of_students = []

    def add_sudent(self, student):
        self.__list_of_students.append(student)
    
    
    def remove_student(self, student):
        self.__list_of_students.remove(student)
        

    def show_course_info(self):
        print("-------------------------------")
        print(f"Course name: {self.__name}")
        print(f"Hours: {self.__hrs}")
        print("List of students: ")
        for st in self.__list_of_students:
            print(st)

s1 = Student("John")
s2 = Student("Jane")

course = Course("OOP", 90)
course.show_course_info()


course.add_sudent(s1)
course.add_sudent(s2)

course.show_course_info()


another_course = Course("Intro to Python", 60)
another_course.add_sudent(s1)
another_course.add_sudent(s2)

another_course.show_course_info()