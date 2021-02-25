#using dictionaries in a program

alien_1 = {'color': 'blue', 'points': 6}
alien_2 = {'color': 'green', 'points': 10}



#lets use the key value pairs to call the aliens attributes
print("\nthe first aliens color is: ", alien_1['color'])
print("\nthe first aliens point value is: ", alien_1['points'])

print("\nthe first aliens color is: ", alien_2['color'])
print("\nthe first aliens point value is: ", alien_2['points'])


#if we want to make use of the aliens values

alien_color1 = alien_1['color'] #here we store just the key value pair of color and assign it to new variable alien_color1
alien_point1 = alien_1['points'] #here we store just the key value pair of the points and assign it the the new variable alien_point1

print(f"\nIf you shootdown a {alien_color1} alien, you will earn {alien_point1} points!")

alien_color2 = alien_2['color'] #here we store just the key value pair of color and assign it to new variable alien_color2
alien_point2 = alien_2['points'] #here we store just the key value pair of the points and assign it the the new variable alien_point2

print(f"\nIf you shootdown a {alien_color2} alien, you will earn {alien_point2} points!")

#now lets combine them in a statement for fun

combined_points = alien_point1 + alien_point2
print(f"\nIf you shootdown both a {alien_color1} and a {alien_color2} alien, you will collect {combined_points} points!")

#now lets create a new dictionary, this time empty parameters

the_alien = {}

#benefit of a empty dictionary is we can now add what we want, when we want without worrying what is in there already.

the_alien['color'] = 'purple'
the_alien['points'] = 20

color = the_alien['color']
score = the_alien['points']


print(f"\nThe new alien we just created is a {color} alien and is worth {score} points!")

#going further with this new alien class lets add x & y coordinates with a speed attribute

the_alien['x_val'] = 0
the_alien['y_val'] = 25
the_alien['speed'] = 'slow'


# print(the_alien) <- this was used to check that the new values were added to the the_alien dictionary

#lets show the original x coordinate
print(f"\nThe original x location of the {color} alien is {the_alien['x_val']}")