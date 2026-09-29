# Program to find the largest of three numbers

num1 = 45
num2 = 72
num3 = 58

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("Largest number:", largest)
