import random
#We are going to set the limits of our data. We want a random number from 1 - 99, and 5 numbers. 
lottery = random.sample(range(1, 99), 5)
#We want to give the user 10 chances to try and guess the number.
chances = 10
guess = 0
#Will use the correct_guess as a list to store correct guesses.
correct_guess = []
correct_guess_count = 0

for number in lottery:
	guess += 1
	print("Guessing Lottery: ", guess)
	while chances > 0:
		print("Remaining chances left: ", chances)
		num = input("Guess lottery number: ")
		if num == number:
			correct_guess.append(num)
			correct_guess_count = correct_guess_count + 1
			print()
			break
		chances = chances - 1
		if chances == 0 and guess != 5:
			print("Chances over! Now try to guess the next number\n")
		chances = 10
		
	print("Total correct guesses: ", correct_guess_count)
	print("The numbers are: ", correct_guess)	



"""
adding text from linux
while count < 5:
    userNumber = int(input("Enter your guess: "))
    count += 1 
    if userNumber < myNumber:
        print("Too small")
    elif userNumber > myNumber:
        print("Too large")
    #if userNumber == myNumber or count == 5:
        #break
    if userNumber == myNumber:
    	print("You guessed it in " + str(count) + " tries")
    elif count > 5:
   		print("You did not guess the number, the number was " + str(myNumber))
"""
