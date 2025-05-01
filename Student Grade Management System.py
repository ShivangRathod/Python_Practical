class Student:
    def __init__(self, roll_no: int, name: str, grades):
        self.roll_no = roll_no
        self.name = name
        self.grades = grades
    
    def get_average(self):
        total_marks = 0
        for subject in self.grades:
            total_marks += self.grades[subject] 
        num_subjects = len(self.grades) 
        return total_marks / num_subjects if num_subjects > 0 else 0
    
    def __str__(self):
        return f"Roll No: {self.roll_no} | Name: {self.name} | Average Marks: {round(self.get_average(), 2)}"

class StudentManager:
    def __init__(self):
        self.students = {}
    
    def add_student(self, roll_no, name, grades):
        self.students[roll_no] = Student(roll_no, name, grades)
    
    def display_student(self, roll_no):
        if roll_no in self.students:
            print(self.students[roll_no])
        else:
            print("Student not found")

n = int(input("Enter number of operations: "))

x = StudentManager()

for i in range(n):
    access = input().split()
    
    if access[0] == "ADD":
        roll_no = int(access[1])
        name = access[2]
        grades = {}
        
        for subject_grade in access[3:]:
            subject, grade = subject_grade.split(":")
            grades[subject] = int(grade)
        
        x.add_student(roll_no, name, grades)
    
    elif access[0] == "DISPLAY":
        roll_no = int(access[1])
        x.display_student(roll_no)
