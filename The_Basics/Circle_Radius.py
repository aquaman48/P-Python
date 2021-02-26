import math
#Here will ask user to input a radius and store it as a float. 
r = float(input("Enter a radius: "))
#Here will set the formulas to calculate the surface area of sphere with given radius
surfaceArea = 4 * 3.14 * r * r
#Calculating for volume 
volume = (4 / 3) * 3.14 * r * r * r
#Calculate for circumference
circumference = 2 * 3.14 * r
#calculate diameter
diameter = 2 * r
#Display results
print("The surface area is ", surfaceArea)
print("The volume is ", volume)
print("The circumference is ", circumference)
print("The diameter is ", diameter)


#taking user input

#1. Ask user to input "radius" of a circle
radius = float(input("Enter Radius: "))
#2. Once input has been received the users input will be put in the formula
area = radius ** 2 * 3.14
#3. After a quick calculation we will then have the area of the circle given the radius we were given by user. 
print("The circle has an area of ", area, "square units!")