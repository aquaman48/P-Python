

#Collect users input of hourly wage, regular hours, and overtime hours for a week of work
wage = float(input("Hourly wage: $"))
hours = float(input("Regular Hours for the week: "))
ot = float(input("Overtime hours: "))
#Insert users input for calculations to find weekly pay
pay = wage * hours
overtime = ot * (wage * 1.5)
totalPay = hours * wage + ot * wage * 1.5

#display weekly pay with given inputs 
print("Your weekly pay is $", + str(round(totalPay, 2)))