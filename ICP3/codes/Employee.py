class Employee:
    Employee_count = 0
    emptotalsal=0
    AverageSal=0;

    def __init__(self, name, family, salary, department):
        self.__name = name
        self.__family = family
        self.__salary = salary
        self.__department = department
        Employee.salary_calculation(salary)


    def salary_calculation(salary):
       Employee.Employee_count = Employee.Employee_count + 1
       Employee.emptotalsal+=salary
       Employee.AverageSal=Employee.emptotalsal/Employee.Employee_count

    def get_name(self):
        return (self.__name)

class PermanentEmployee(Employee):
    def __init__(self, name, family, salary, department):
     Employee.__init__(self, name, family, salary, department)


Employee1 = Employee("A","FamilyA",10000000,"Python")
Employee2 = Employee("B","FamilyB",20000000,"Programming")
PermanentEmployee1 = PermanentEmployee("C","FamilyC",40000000,"BDP")
print("Number of employees is:", Employee.Employee_count)
print("Average salary is:", Employee.AverageSal)
print("name of permanent employee is:", PermanentEmployee.get_name(PermanentEmployee1))
