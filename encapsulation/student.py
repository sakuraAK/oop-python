class Student:
    def __init__(self, name):
        self.__name = name
        self.__grades = []

    def add_grade(self, grade):
        if grade >= 0 and grade <= 100:
            self.__grades.append(grade)
        else:
            print(f"Warning: {grade} is not a valid grade")

    def get_average(self):
        if len(self.__grades) > 0:
            return sum(self.__grades) / len(self.__grades)
        else:
            return -1
    
    def display_average(self):
        average = self.get_average()
        if average >= 0:
            print(f"The average of {self.__name} is {self.get_average()}")
        else:
            print(f"Student {self.__name} doesn't have grades yet")


student_1 = Student("Jane D")

student_1.add_grade(85)
student_1.add_grade(90)
student_1.add_grade(500)

student_1.display_average()