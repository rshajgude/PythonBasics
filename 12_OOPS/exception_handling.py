from json.encoder import INFINITY
class MyCustomEx(Exception):
    pass

a=input("Enter number 1 : ")
b=input("Enter number 2 : ")
c=None

try:
    if int(a) > 100 :
        raise ValueError("Value should not be a > 100 or b > 50")
    if int(b) > 50 :
        raise MyCustomEx("You need to enter b<50")
    c=int(a)/int(b)
except ZeroDivisionError as zde:
    print(f"exception occurred : ", zde)
except TypeError as te:
    print(f"exception occurred : ", te)
except ValueError as ve:
    print(f"exception occurred : ", ve)
except Exception as e:
    print(f"Generic exception occurred : ", e)
finally:
    print("Finally block which is executed after exception is occurred or not occurred")
print(f"value of c is {c}")