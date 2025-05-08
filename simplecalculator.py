print('''
+ Add
- Subtract
* Multiply
/ Divide
''')
num1=int(input("enter 1st number :"))
num2=int(input("enter 2nd number :"))
opr=input("enter operator:")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("invalid operation")
