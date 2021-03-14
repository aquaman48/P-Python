

#Creating lists are done like this. listName = ['listItem0','ListItem1',...'etc']
pokemon = ['charizard', 'pikachu', 'arcanine', 'amoongus']

#printing the list we created
print(pokemon)

#Using the list items index we can specify a specific item to print, index 0 would be charizard. Remember index starts a 0
print(pokemon[0])
print(pokemon[1])
print(pokemon[2])
#We can use .title to cause the first letter to be capitilized. 
print(pokemon[1].title())
#We can also use [-1] to display the last item in the list
print(pokemon[-1].title())

#We can even display our values within a message to the user. Remember use {} to enclose your variable.  
message1 = f"The first Pokemon I ever caught was a {pokemon[1].title()}!"
battle1 = f"The first Pokemon battle I ever watched was\n{pokemon[1].title()} versus {pokemon[0].title()}"
message2 = f"Coming up is {pokemon[2].upper()} versus {pokemon[3].lower()}!"
print(message1)
print(battle1)
print(message2)

#Here I will add 2 list items as a variable and then another statment to display them in a combined statement
teamA = pokemon[0].title(), pokemon[1].title()
teamB = pokemon[2].title(), pokemon[3].title()
showdown = f"The moment you all have been waiting for!\nWe have the ferocious fire lightning combo\n{teamA}\nversus\n{teamB}"
#Probably not the best way to really display the results but it does work. 
print(showdown)

#If we want to change values then we create a variable of that with value index and then print it
pokemon[1] = 'raichu'
print(pokemon)
#Moving on here we can use the .append to add additional items to the list, it will get added to the end of our list
pokemon.append('venusaur')
print(pokemon)

#Another way to change list data is with .insert and we declare which index to replace. As you can now we added pikachu back and will keep raichu as well
pokemon.insert(1, 'pikachu')
print(pokemon)

#To delete a index we will use del and declare the value, we can see now raichu is gone
del pokemon[2]
print(pokemon)

#if we want to remove an item but still want to use it we can use pop()

popped_Pokemon = pokemon.pop()
print(pokemon)
print(popped_Pokemon)