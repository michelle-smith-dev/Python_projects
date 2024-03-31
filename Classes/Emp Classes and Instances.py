class Employee:
    # init method is the constructor of the class. This takes the class as the first argument. Can be named anything but
    # convention is to use 'self'
    def __init__(self, first, last, pay):
        # self is the instance
        # Instance variables:
        self.first = first  # This is the same as using: emp_1.first = 'Corey', to create an instance using the class
        # see below example of calling the class with this instance.
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# emp_1 = Employee()
# emp_1.first = 'Corey'
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Jane', 'Smith', 60000)

# The 2 call methods below are doing exactly the same. One is passing the instance name, and this can be done since the
# method takes 'self' as an argument. The other is calling the class name, so it knows exactly which class to use, and
# passes the instance name
print(emp_1.fullname())  # since we are using the instance name to call the method, it gets passed as the argument
print(Employee.fullname(emp_1))  # I have to pass emp_1 as an argument because it doesn't know what instance to use

# print(emp_2.email)
# print(emp_2.fullname())

