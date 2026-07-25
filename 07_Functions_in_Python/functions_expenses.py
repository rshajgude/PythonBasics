expenses_1=[32,46,234,1553,94]
expenses_2=[8,392,34,234,23]

def sum_list(expenses):
    '''
    :param expenses: input list of numbers
    :return: total of all numbers in list
    '''
    total=0
    for expense in expenses:
        total+=expense
    return total

print(f"Sum of all items : {sum_list(expenses_1)}")
print(f"Sum of all items : {sum_list(expenses_2)}")

