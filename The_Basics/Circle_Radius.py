#Week 1 Question 4 pg. 62

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