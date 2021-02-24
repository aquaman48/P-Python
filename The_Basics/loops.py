"""
The objective is to randomly generate 5 lottery numbers that range from 1 - 99
We want to receive the users input as a guess and will give them 10 tries for each randomly generated number
"""
#Use import random to generate random numbers
import random
#Generate the 5 random numbers with range of 1 - 99
winningLottery = random.sample(range(1, 99), 5)
ticket1 = winningLottery
ticket2 = winningLottery
ticket3 = winningLottery 

winningTicket = ticket1, ticket2, ticket3
#Initialize how many chances we are giving 
chanceGuess = 10
#guessedNum will be for the count of guessed numbers for each loop
guessedNum = 0
#if the user gets the number right we will store it in the correctGuess list and use correctGuessCount to count how many we got right
correctGuess = []
correctGuessCount = 0

#Brief introduction describing what we want from user and what they should expect
print("Hello and welcome to my LUCKY lottery ticket!\nI want to give you a chance to guess 5 numbers\nThe range of these numbers will be 1 - 99\nYou will be given 10 chances for each number!\nGood luck!")
#here is where we will start the outer loop 
for number in winningTicket:
	guessedNum += 1
	print("Guessing Number: ", guessedNum)
	#here is where we will add the inner loop 
	while (chanceGuess > 0):
		print("You have ", chanceGuess,"tries left!")
		randNum = input("What is your guess: ")
		if userNum == winningTicket:
			correctGuess.append(userNum)
			correctGuessCount = correctGuessCount + 1
			print("Nailed IT!")
			break
		chanceGuess = chanceGuess - 1
		if chanceGuess == 0 and guessedNum != 5:
			print("Nice try, looks like you didn't get it\nYou can do it!")
	chanceGuess = 10
print("Total numbers you got correct are: ", correctGuess)
print("The winning numbers are: ", winningTicket)
