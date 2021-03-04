"""
Prints the average of the numbers in a text file 

"""

from functools import reduce

# Accept the input file name and open the file
fileName = input("Enter the input file name: ")
inputFile = open(fileName, 'r')

# Read the numbers as strings into a list
lyst = []
for line in inputFile:
    lyst.extend(line.split())

# Convert all the strings in the list to numbers
lyst = list(map(float, lyst))

# Compute the sum of the numbers
summation = reduce(lambda x, y: x + y, lyst)
minimum = min(lyst)
maximum = max(lyst)
def averages():
	# Print the average
	if len(lyst) == 0:
		average = 0
	else:
		average= summation / len(lyst)
		print("The average is", average)

def minimums():
	if len(lyst) == 0:
		minimum = 0
	else:
		minimum = min(lyst)
		print("The minimum is", minimum)


def maximums():
	if len(lyst) == 0:
		maximum = 0
	else:
		maximum = max(lyst)
		print("The maximum is", maximum)


averages()
minimums()
maximums()