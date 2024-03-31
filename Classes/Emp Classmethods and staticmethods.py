class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # Instance variables:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):  # cls is the default argument naming convention
        cls.raise_amount = amount

    @classmethod  # Let's take the manual method below, and turn into a class method to split an employee string that
    # uses a hyphen as a separator
    def from_string(cls, emp_str):
        frst, lst, py = emp_str.split('-')
        return cls(frst, lst, py)

    @staticmethod  # staticmethod is used when it makes logical sense to group with the class but doesn't depend on
    # any instance or class variable
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


import datetime  # python datetime module assigns the days of the week, 0 - 6, with Monday = 0, Sunday = 6
my_date = datetime.date(2023, 7, 10)

print(Employee.is_workday(my_date))

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)
emp_1.raise_amount = 1.06  # This is setting a different raise amount for the emp_1 instance
Employee.set_raise_amt(1.07)  # Because this is calling the set_raise_amt classmethod, this amount passed gets set at
# the class level instead of instance level

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Let's say we need to parse a string separated by a hyphen to create a new employee. Here is the manual way to
# accomplish that task:
emp_str_3 = 'John-Doe-70000'
emp_str_4 = 'Steve-Johnson-30000'

'''first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)
'''

new_emp_3 = Employee.from_string(emp_str_3)
print(new_emp_3.email, new_emp_3.pay)
