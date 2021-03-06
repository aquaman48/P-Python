"""
Week 3 Chapter 6 Project 2 
Nicholas Waterman

"""

import math

#initialize the tolerance
TOLERANCE = 0.000001

def newton(x, estimate):
	"""Perform the successive approximations"""
	difference = abs(x - estimate ** 2)
	if difference <= TOLERANCE:
		return estimate
	else:
		"""Recursive after improving the estimate"""
		return newton(x, (estimate + x / estimate) / 2)


def main():
	while True:
		x = input("Enter a positive number or press enter/return to quit: ")
		if x == "":
			break
		x = float(x)
		print("The programs estimate is", newton(x,1))
		print("Python's estimate is    ", math.sqrt(x))

if __name__ == '__main__':
	main()