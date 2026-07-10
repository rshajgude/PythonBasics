
expenses=[1242, 6210, 1032, 4300, 102, 4253]

# travers entire list
for expense in expenses:
    print(expense)

# Add each element from list to total
total=0
for expense in expenses:
    total=total+expense

print(f"Total expenses are {total}")

# Enumerate function usage
for idx, expense in enumerate(expenses):
    print(f"expense at index {idx} are {expense}")

# break in for loop
threshold=1000
for idx, expense in enumerate(expenses):
    if expense<threshold:
        print(f"Expense are less in month {idx} with expense {expense}")
        break

# Zip
expenses=[1242, 6210, 1032, 4300, 102, 4253]
months= ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
threshold=1000
for tp in zip(expenses, months):
    print(tp)

for expense, month in zip(expenses, months):
    if expense<threshold:
        print(f"Expense are less in month {month} with expense {expense}")
        break

# Nested for loop
for i in range(5):
    for j in range(5):
        print(i,j)

# For else

for i in range(5):
    print(i)
else:
    print("For loop completed")

for i in range(5):
    if i>2:
        break
    print(i)
else:
    print("For loop completed after break")