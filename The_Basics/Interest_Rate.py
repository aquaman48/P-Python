"""
Nicholas Waterman

"""
ANNUAL_RATE = .12
MONTHLY_RATE = ANNUAL_RATE / 12

#Take users input 
purchasePrice = float(input("Please enter price of item:"))

monthlyPayment = .05 * purchasePrice
month = 1
balance = purchasePrice
print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")
while balance > 0:
	if monthlyPayment > balance:
		monthlyPayment = balance
		interest = 0
	else:
		interest = balance * MONTHLY_RATE
	principal = monthlyPayment - interest
	remaining = balance - monthlyPayment
	print("%2d%15.2f%15.2f%17.2f%17.2f%17.2f" % \
		(month, balance,interest, principal, monthlyPayment, remaining))
	balance = remaining
	month += 1



