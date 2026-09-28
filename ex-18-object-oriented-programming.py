class Student:
    """学生"""
    def __init__(self, age, name):
        self.name = name
        self.age = age
        
    def study(self, course_name):
        print(f'正在学习{course_name}.')

    def play(self):
        print(f'学生正在游玩.')


stu1 = Student(20,'tom')
stu2 = Student(22,'nancy')
Student.study(stu1, 'Python')
stu2.study('cpp')