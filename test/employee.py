class Employee():

    def __init__(self,employeeID, name):
        self.employeeID=employeeID
        self.name=name
    def printvariables(self):
        print(self.employeeID,self.name)

emp1=Employee(1,"sin")
emp1.printvariables()
