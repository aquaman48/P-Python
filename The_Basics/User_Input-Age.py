

#1. Ask user to input name and store it as text string
name = input("Enter your name: ")
#2. Ask user to input age and store it as an int var.
age = int(input("Enter your age: "))
#3. Displays users input of name and age. 
print("\nHello,",name,". \nToday you told me you are ", age,"years old")


#more fun with user input

first = int(input("Please enter the smaller integer: "))
second = int(input("Please enter the larger integer: "))

while first > 0:
	remainder = second % first
	second = first
	first = remainder

print("The greatest common divisor is", second)