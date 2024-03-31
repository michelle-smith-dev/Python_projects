class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10  # 10 percent

    def __init__(self, first, last, pay, prog_lang):  # add prog_lang value to pass through this sub class
        super().__init__(first, last, pay)  # Let the Employee class handle the first, last and pay arguments
        # Employee.__init__(self, first, last, pay)  # This does the same thing as super; can use either but using super
        # is more maintainable, especially when using multiple subclasses and inheritances
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):  # You never want to set a mutable data type such as lists or
        # dicts as default arguments. This is why the employees=None
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Jane', 'Smith', 60000, 'Java')

# Test Manager subclass
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])  # Must pass the variable employee in a list,
# since employee is not none, it will return the employee, and it can't return the variable
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

# Test built-in functions isinstance and issubclass
print(isinstance(mgr_1, Manager))  # isinstance mgr_1 variable of the Manager class
test = 23
print(isinstance(test, int))  # is instance this or that, so this is asking, isinstance test variable an integer type
print(isinstance(mgr_1, Developer))  # False, the mgr_1 variable calls the Manager subclass and therefore is not in
# Developer subclass. But it is part of the Employee class, since Employee is the parent class.
print(isinstance(dev_1, Manager))  # False, dev_1 is only part of Employee class and developer subclass
print(issubclass(Manager, Employee))  # True, Manager is a subclass of Employee
print(issubclass(Manager, Developer))  # False, Manager is not a subclass of Developer, as they are both subclasses

# Test Developer subclass
# print(dev_1.pay)
# dev_1.apply_raise()  # Because we have the dev_1 calling the Developer class, it will run through that sub class, which
# # has the raise amount set to 10%. If we changed dev_1 to call the Employee class, then it would use the 4% raise amount
# print(dev_1.pay)

# Test developer prog_lang argument
# print(dev_1.email)
# print(dev_1.prog_lang)

# print(help(Developer))
