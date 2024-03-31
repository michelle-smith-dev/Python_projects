class Employee:
    # Class variables are shared across all instances
    # Instance variables are unique to that instance
    num_of_emps = 0
    raise_amount = 1.04  # When we access these class variables, using them in any method below, we need to access them
    # through the class itself or an instance of the class. i.e., use Employee.raise_amount or self.raise_amount

    def __init__(self, first, last, pay):
        # Instance variables:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1  # Come back to this concept for testing

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):  # Because this is something that could be used for all instances as a standard raise amount,
        # we can make it a class variable instead of hard coding a value to multiply self.pay with.
        self.pay = int(self.pay * self.raise_amount)  # Can either call the class with Employee.raise_amount, or can set
        # to self.raise_amount, which will allow you to set the raise amount with a unique instance



emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)
emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.__dict__)
print(emp_2.raise_amount)
print(Employee.num_of_emps)
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

