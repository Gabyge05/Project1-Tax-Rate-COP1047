#The costumer request a program that computes a person's income tax
#  
#All taxpayers are charged a flat tax rate of 20 % 
#All taxpayers are allowed a $ 10,000 standard deduction
#For each dependent, a taxpayer is allowed an additional $ 3,000 deduction
#Gross income must be entered to the nearest penny
#The income tax is expressed as a decimal number 

# Set variables 
tax_rate = 0.20
standard_deduction = 10000
each_dependent = 3000

# Getting input from the costumer
gross_income = float(input('Enter the gross income: '))
number_of_dependents = int(input('Enter the number of dependents: '))

# Calculate Income Tax
taxable_income = gross_income - standard_deduction - (each_dependent * number_of_dependents)
income_tax = taxable_income * tax_rate

# Getting output 
print(' The income tax is $ ',str(income_tax))