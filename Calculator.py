a = int(input("Enter num 1: "))
b = int(input("enter num 2: "))
choice = input("Enter the choice: ")
Addition = a+b
Subtraction = a-b
Multiplication = a*b
Division = a/b
Modulous = a%b

if choice=='+':
    print( Addition)
elif choice=='-':
    print(Subtraction)
elif choice=='*':
    print(Multiplication)
elif choice=='/':
    print(Division)
elif choice=='%':
    print(Modulous)
else: print("invalid: ")
    