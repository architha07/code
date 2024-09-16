class Employee:
    raise_amount=1.04
    num_emp=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last +'company.com'

    def fullname(self):
        return '{} {}'. format(self.first, self.last)
    def apply_raise(self):
        self.pay=int(self.pay*Employee.raise_amount)

emp_1=Employee('alex','alex',50000)
emp_2=Employee('test','user',40000)
print(emp_1.pay)
emp_1.apply_raise()
print(Employee.raise_amount)
print(Employee.num_emp)



