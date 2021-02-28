"""
1. Write a Python script to concatenate following dictionaries to create a new one. 
2. Write a Python script to check if a given key already exists in a dictionary.
3. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
"""

#Start of dictionary variables and then concatenating them.
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

mergeDic = {**dic1, **dic2, **dic3}
print(mergeDic)

#Write a script to check if given key already exists
key = 4 
if key in mergeDic.keys():
	print("\nThe key ", key, "exists in the dictionary!")

#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = 5 
squareDic = {x:x*x for x in range(1, n+1)}
print(squareDic)