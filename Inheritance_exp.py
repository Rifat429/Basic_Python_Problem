class User:
    def login(self):
        print("please login")
    
    def register(self):
        print("Please register")

class Student(User):

    def enroll(self):
        print("Enroll")
    
    def review(self):
        print("give feedback")
    
class Teacher(User):

    def course(self):
        print("your courses")
    def answer(self):
        print("answers")



std1= Student()
std1.review()
std1.enroll()

teach1= Teacher()

teach1.login()
teach1.answer()