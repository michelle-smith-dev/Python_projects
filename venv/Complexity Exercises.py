# (1) try to figure it out without running it
#     write down the first few inputs/outputs
#     try to graph it if applicable
# (2) run it to try to gain insight from the output
# (3) look up the answer or ask to work through it next class

def fn1(n):
    for i in range(n):
        print(i)
'''
Time complexity would be O(n), because the range(n) could be any amount and will depend on that size.
'''

def fn2(n):
    for i in range(n):  # O(n)
        for j in range(n):  # O(n)
            print((i, j))
'''
So if both lines in this function are linear, does this make it O(n) because it's based on 'n', or is it 'n squared' since it's two separate lines of code that depend on an 'n' value?
GOOGLE shows that a nested for loop is O(n2)
'''

def fn3(n):
    print(n) # O(1)
    while n > 0:  # O(1)
        n = n//2  # O(n) # O(1)
        print(n)  # O(1)
'''
Look at what the process is doing. In this case, it is cutting 'n' in half multiple times. This will mean it is using O(log n)
time complexity. (default is in base 2, but this could be log3n if this were dividing the 'n' by 3)
'''

def fn4(n):
    x = 0  # O(1)
    print(x)  # O(1)
    while x < n:  # O(1)
        x = x * 2  # O(1)
'''
Since the process is multiplying, it will use O(n log n)
'''




# import math
#
# print(math.log2(1))

