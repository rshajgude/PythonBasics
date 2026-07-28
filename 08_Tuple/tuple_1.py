


marks=(13,12,16,23)

print(type(marks))

def double_it(a,b):
    # Its always a good practice to return a tuple from function called
    # As tuple is same as list just its immutable
    return a*2, b*2

c, d = double_it(5,2)
print(c, d)