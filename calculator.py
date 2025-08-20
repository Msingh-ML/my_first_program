
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = (input("Enter an operation (+, -, *, /): "))
if(c == "+"):
    d = a + b
elif(c == "-"):
    d = a - b
elif(c == "*"):
    d = a * b
else:
    d = a / b

print("result: ", d)