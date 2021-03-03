"""
Reads from Unique.txt file 

"""

#Take input file name
inName = input("Enter the input file name: ")

#Open the input file and initialize list of unique words
inputFile =  open(inName, 'r')
uniqueWords = []

#Add the unique words in the file to the list
for line in inputFile:
	words = line.split()
	for word in words:
		if not word in uniqueWords:
			uniqueWords.append(word)
uniqueWords.sort()

#Prints unique words
for word in uniqueWords:
	print(word)