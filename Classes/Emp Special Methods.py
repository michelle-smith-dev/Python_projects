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

    def __repr__(self):  # return something here that can recreate the object
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):  # At a minimum, have __repr__ defined, because if __str__ is not defined, it will automatically
        # fall back to use repr by default
        return '{}: {}'.format(self.fullname(), self.email)

    # create special dunder add method to add two employees salaries together
    def __add__(self, other):  # self is left side of addition and other is the right side of addition
        return self.pay + other.pay

    def __len__(self):  # return length of the full name when passing an emp instance
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)

# If both str and repr are defined, just printing the instance below will use the str method
print(emp_1)  # Since we have the __repr__ method, now printing this variable will print out with the format defined in
# the __repr__ method

# You can specifically reference those two methods and pass our instance with it to get the output
print(repr(emp_1))
print(str(emp_1))
# These print statements will print out the exact same thing below
print(emp_1.__repr__())
print(emp_1.__str__())

# using the built-in dunder add method
print(int.__add__(1,2))  # adds the numbers, prints 3
print(str.__add__('a', 'b'))  # concatenate the letters, prints 'ab'

# Using the created special dunder add method I created above:
print(emp_1 + emp_2)  # If you remove the dunder add method created and try to run this, it will give you a type error

# Test built-in len method and the created dunder len method
print(len('test'))  # This will get the length on the string you're passing through because len is a built-in function
print(len(emp_1))  # if the created dunder len method is not created, you will get a type error trying to print this way

