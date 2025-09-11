## This program serves as a personal finance calculator

monthly_income = int(input('Enter your monthly income: '))
monthly_expense = int(input('Enter your total monthly expenses: '))

monthly_saving = monthly_income - monthly_expense

annual_saving = monthly_saving * 12 + (monthly_saving * 12 * 0.05)

print(f'Your monthly savings are {monthly_saving}.')
print(f'Projected savings after one year, with interest, is: {annual_saving}')
