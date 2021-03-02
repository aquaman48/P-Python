"""

Print a payroll report.

Input
   A file in which each line has the form
   
   <last name> <hourly wage> <hours worked>

Output
   A report in tabular format.  Each line has the form

   <last name> <hours worked> <total wages>
   
"""

# Take the inputs
fileName = input("Enter the file name: ")

# Open the input file
inputFile = open(fileName, 'r')

# Read the data and print the report
print("%-15s%15s%15s%20s%15s" %("Name", "Hours", "Total Pay","Employee Number", "Address"))
for line in inputFile:
    dataList = line.split(',')
    name = dataList[1]
    hours = float(dataList[2])
    payRate = float(dataList[3])
    address = dataList[4]
    totalPay = hours * payRate
    print("%-15s%10d%15.2f%15s%20s" %(name, hours, totalPay, dataList[0], dataList[4]))


print("Thank you for checking out a simple payroll!")

    
