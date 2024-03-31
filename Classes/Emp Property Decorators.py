class Employee:

    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # allows us to define a method, but we can access it like an attribute
    def email(self):  # We can create the email method, which would properly handle an employee name change, but then
        # you would have to update any calls made using the email to a method call
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')  # split the name string that is passed as the name argument
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'
# If we want to change the first name, when we print the email, because it's not a method, it will print with the first
# instance we pass through, which is John Smith and not the updated Jim Smith

# This will not work and we have to use a setter
emp_1.fullname = 'Michelle Smith'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.fullname)