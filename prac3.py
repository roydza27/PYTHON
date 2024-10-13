def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return float(x*y)

def divide(x,y):
    return float(x/y) 

def error(x,y):
    global ch
    try :
        r=x/y

    except ValueError:
        print("Enter Numeric Value ")
    except ZeroDivisionError:
        print("Error! Division By Zero is not Allowed")

while True:
    num1=int(input("Enter First Number : "))
    num2=int(input("Enter Second Number : "))
    ch=int(input("Enter Operation :\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\nEnter Choice : "))

    if ch == 1:
        print(f"\nAddition : {add(num1,num2)}\n")
    elif ch == 2:
        print(f"\nSubstraction : {subtract(num1,num2)}\n")
    elif ch == 3:
        print(f"\nMultiplication : {multiply(num1,num2)}\n")  
    elif ch == 4:
        print(f"\nDivision : {divide(num1,num2)}\n")
    excep=error(num1,num2)

    c=input("Continue : y/n ")
    if c.lower() != "y":
        break
