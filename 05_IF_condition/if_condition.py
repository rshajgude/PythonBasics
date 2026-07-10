
n=input("Enter a number of your choice : ")
print(n)
n=int(n)

if n%2==0:
    print("Number is an even")
else:
    print("Number is an odd")

#message="Number is an even" if n%2==2 else "Number is an odd"
#print(message)

marks=45

print(f"You got {marks} marks and ..")
if marks>75:
    print("You got distinction")
elif marks>65:
    print("You got first class")
elif marks>50:
    print("You are passed with second class")
elif marks>35:
    print("You are passed")
else:
    print("You are failed..!")