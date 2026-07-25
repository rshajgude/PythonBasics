
# You want to have flexibility to have diff argument list with diff count
def sum_all(*args):
    print("inside sum_all")
    total=0
    print(args)
    print(type(args))
    for i in args:
        total+=i
    return total

print(sum_all(1,2,3))
print(sum_all(1,2,3,4))
print(sum_all(1,2,3,4,5))
