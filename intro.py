class student:
    def __init__(self,name,age,grade):
        self.name =name
        self.age=age
        self.grade=grade
    def output(self):
        print(f"the student name {self.name} { self.age} has {self.grade} grade! ")
        
s1=student("mgmg",23,"A")
s2=student("hlahla",22,"E")
s3=student("myamya",23,"C")

s1.output()
s2.output()
s3.output()