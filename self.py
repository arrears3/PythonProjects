class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Hello, my name is " +self.name)
Person1 = Person("Ria",289)
Person1.display()