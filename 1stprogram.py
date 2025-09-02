# This is my first python program
a = int(input("enter a number: "))
b = int(input("enter another number: "))
c = a + b
print("The sum of", a, "and", b, "is ", c)

# Arithmetic operations
side = int(input("Enter the length of a side of the square: "))
area = side * side
print("The area of the square is", area)

# Average of two numbers
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
avg = (a + b) / 2
print("The average of", a, "and", b, "is", avg)

# Comparison operators
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
bool = a >= b
print("The first number is greater than or eaqual to the second:", bool)

# Strings
# length of a string
name = input("Enter first your name: ")
print(len(name))

# counting specific character in a string
a = input("any sentence with $")
print("no of $ in this sentence is ", a.count("$"))

# conditional statement
# grading system
marks = int(input("Enter your marks : "))
if(marks >= 90):
    print("Grade A")
elif(90 > marks >= 80):
    print("Grade B")
elif(80 > marks >= 70):
    print("Grade C")
else:
    print("Grade D") 

# even or odd
num = int(input("enter number "))
if(num % 2 == 0):
    print("number is even")
else:
    print("number is odd")

# biggest of three numbers
a = int(input("enter 1st number "))
b = int(input("enter 2nd number "))
c = int(input("enter 3rd number "))
if(a >= b and a >= c):
    big = a
elif(b >= c):
    big = b
else:
    big = c

print("biggest number is ", big)

# multiple of 7
num = int(input("Enter a number "))
if(num % 7 == 0):
    print(num,"is a multiple of 7")
else:
    print(num,"is not a multiple of 7")