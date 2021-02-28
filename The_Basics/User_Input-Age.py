

#1. Ask user to input name and store it as text string
name = input("Enter your name: ")
#2. Ask user to input age and store it as an int var.
age = int(input("Enter your age: "))
#3. Displays users input of name and age. 
print("\nHello,",name,". \nToday you told me you are ", age,"years old")



#more fun with user input

print("\n\n\n\nFinding the Greatest Common Divisor between two numbers. Get 2 numbers in your mind and prepare them!")
first = int(input("\nPlease enter the smaller integer: "))
second = int(input("\nPlease enter the larger integer: "))

while first > 0:
	remainder = second % first
	second = first
	first = remainder

print("\nThe greatest common divisor is", second)

#adding user input to find sum

theSum = 0
count = 0
while True:
	number = input("Enter a number or press Enter to quit: ")
	if number == "": 
		break
			theSum += float(number)
			count += 1

print("The sum is", theSum)
if count > 0:
	print("The average is", theSum / count)


#Using a loop for a 'countdown'

countdown = 5
while countdown > 0:
	print(countdown)
	countdown = countdown - 1
print("Blast off!!!!")

