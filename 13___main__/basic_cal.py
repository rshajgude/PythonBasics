
def double_it(a):
    print("Value of __name__", __name__)
    return a*2

def triple_it(b):
    print("Value of __name__", __name__)
    return  b*3

def square_it(c):
    print("Value of __name__", __name__)
    return c**2

# Test calls to functions defined above, all are executed everytime we import file
print(double_it(5))
print(triple_it(7))
print(square_it(10))