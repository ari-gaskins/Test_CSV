# import csv
from datetime import datetime, date

date_in = input('Enter the date: ')
date_out = datetime.strptime(date_in, '%m/%d/%Y')
date_out = date_out.date()
gross_income = input('Enter gross income: $')
gross_income = int(gross_income)
tax = gross_income * 0.153
total_income = gross_income - tax

print(f'The date is: {date}, the gross income is: {gross_income}, the tax is: {tax}, and the total income is: {total_income}.')


