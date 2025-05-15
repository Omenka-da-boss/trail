# print("Hello World")

# name =  input("Enter your name: ")
# print(f"Welcome back {name}")


class Animal:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def hello(self):
        print(f"Hello {self.name}")
    
    def goodbye(self):
        print(f"Goodbye {self.name}")
    
    def check(self):
        if self.age >= 20:
            print(f"Welcome to this page you are eliglbe")
        else:
             print(f"Come back when you are up to 20")

student = Animal("Omenka",22)

print(student.name)
student.check()