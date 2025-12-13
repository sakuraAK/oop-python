class Student:
    # name and major
    
    def __init__(self, name, major):
        self.__name = name
        self.__major = major
        
    
    @property
    def name(self):
        return self.__name
    
    @property
    def major(self):
        return self.__major
    
    def __str__(self):
        return f"Student. Name: {self.__name}, Major: {self.__major}"
    


class Course:

    def __init__(self, name):
        self.__name = name
        self.__list_of_students: list[Student] = []

    def add_student(self, student: Student):
        self.__list_of_students.append(student)
    
    def remove_student(self, student: Student):
        for course_student in self.__list_of_students:
            if course_student.name == student.name:
                # remove student from the list
                self.__list_of_students.remove(course_student)

    def print_all_students(self):
        for student in self.__list_of_students:
            print(student)
            
            
    def print_stats(self):
        
        major_cnts = {}
        
        for student in self.__list_of_students:
            if not student.major in major_cnts:
                major_cnts[student.major] = 0
            major_cnts[student.major] = major_cnts[student.major] + 1
        print(f"Course: {self.__name}")
        print("----------------------------")
        for k, v  in major_cnts.items():
            print(f"{v} students from {k}")
                
                    
        
    
    

student1 = Student("John", "Biology")
student2 = Student("Jane", "Computer Science")
student3 = Student("Percy", "Chemical Engineering")
student4 = Student("Dave", "Computer Science")

course = Course("OOP Programming")

course.add_student(student1)
course.add_student(student2)
course.add_student(student3)
course.add_student(student4)


course.print_all_students()

course.print_stats()

course1 = Course("Intro to Programming Languages")

course1.add_student(student1)
course1.add_student(student2)