class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades 

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}")

    def calculate_average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0


class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):

        for student in self.students:
            student.display_info()

    def calculate_average_grades(self):
        total_average = 0
        
        for student in self.students:
            total_average += student.calculate_average_grade()
        if self.students:
            return total_average / len(self.students)
        return 0


if __name__ == "__main__":
    db = StudentDatabase()

    student1 = Student("Alice", 20, [85, 90, 88])
    student2 = Student("Bob", 22, [78, 82, 80])
    student3 = Student("Charlie", 21, [95, 92, 94])

    db.add_student(student1)
    db.add_student(student2)
    db.add_student(student3)

    print("All Students:")
    db.display_all_students()

    average_grades = db.calculate_average_grades()
    print(f"\nAverage Grade of All Students: {average_grades}")