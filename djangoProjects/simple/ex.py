interestRate = 6/(100*12)
print(interestRate)
numberOfMonths = 12
lounAmount = 2500000
monthlyPayment = lounAmount * ((interestRate ) /( 1- (1+interestRate)**(-numberOfMonths)))
print(monthlyPayment)

