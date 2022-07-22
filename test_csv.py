import csv
from datetime import datetime, date

# create variables for data inputs
date_in = input('Enter the date: ')
date_out = datetime.strptime(date_in, '%m/%d/%Y')
date_out = date_out.date()
gross_income = input('Enter gross income: $')
gross_income = round(int(gross_income), 2)
tax = round(gross_income * 0.153, 2)
total_income = gross_income - tax

#print(f'The date is: {date_out}, the gross income is: {gross_income}, the tax is: {tax}, and the total income is: {total_income}.')

# set csv header
header = ['Date', 'Gross Income', 'Tax', 'Total Income']

# set csv data
data = [
    [date_out, gross_income, tax, total_income]
]

# open csv
with open('income.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write header to csv
    writer.writerow(header)

    # write data to csv
    writer.writerow(data)