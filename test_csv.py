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
    {'Date': date_out, 
    'Gross Income' : gross_income,
    'Tax' : tax,
    'Total Income' : total_income}
]

# open csv
with open('income.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header)

    # write header to csv
    writer.writeheader()

    # write data to csv
    writer.writerows(data)

    # close csv file
    f.close()