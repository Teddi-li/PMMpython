class manager:
    def salary(self):
        print("this is your slaray for the month and keep trying!!!")
class employee(manager):
    def salary(self):
        print("is this all??")

a=manager()
b=employee()
 
a.salary()
b.salary()