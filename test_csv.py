# import csv
from datetime import datetime, date

date_in = input('Enter the date: ')
date_out = datetime.strptime(date_in, '%m/%d/%Y')
date_out = date_out.date()
gross_income = input('Enter gross income: $')
gross_income = round(int(gross_income), 2)
tax = round(gross_income * 0.153, 2)
total_income = gross_income - tax

print(f'The date is: {date_out}, the gross income is: {gross_income}, the tax is: {tax}, and the total income is: {total_income}.')


