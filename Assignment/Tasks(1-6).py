# Banking System

# Task-1
'''
credit_score = int(input("Enter the credit score: "))
annual_income = float(input("Enter the annual_income: "))

if credit_score > 700 and annual_income >= 50000:
    print("Customer is eligible for loan")
else:
    print("Customer is not eligible for loan")
'''

# Task-2
'''
print("1.Check balance")
print("2.Withdraw")
print("3.Deposit")

choice = int(input("Enter your choice: "))
curr_balance = float(input("Enter current balance: "))

if choice == 1:
    print(f'Your current balance is {curr_balance}')
elif choice == 2:
    withdrawal_amount = float(input('Enter amount to withdraw: '))
    if withdrawal_amount > curr_balance:
        print("Insufficient Funds")
    elif withdrawal_amount % 100 != 0 or withdrawal_amount % 500 != 0:
        print('Withdrawal amount must be in multiples of 100 or 500')
    else:
        curr_balance -= withdrawal_amount
        print(f'Withdrawal successful. Current Balance is {curr_balance}')
elif choice == 3:
    deposit_amount = float(input("Enter deposit amount: "))
    curr_balance += deposit_amount
    print(f"Deposit successful. Current balance is {curr_balance}")
else:
    print("Invalid choice")
'''

# Task-3
'''
no_of_customers = int(input('Enter the number of Customers: '))
for customer in range(no_of_customers):
    initial_balance = float(input('Enter the initial balance: '))
    interest_rate = float(input('Enter the annual interest rate: '))
    years = int(input('Enter the number of years: '))
    future_balance = initial_balance * ((1 + (interest_rate/100)) ** years)
    print(f'Future Balance for customer{customer} is {future_balance}')
'''

# Task-4
'''
no_of_customers = int(input("Enter number of customers: "))
for customer in range(no_of_customers):
    acc_no = int(input('Enter your valid account number: '))
    balance = float(input('Enter your balance: '))
    if len(str(acc_no)) == 11:
        if str(acc_no).isdigit():
            print(f'The balance of customer {customer} is {balance}')
    else:
        print("Invalid account number")
'''

# Task-5
'''
password = input("Enter your password: ")
if len(password) < 8:
    print("Invalid Password. Password should not be less than 8 characters.")
elif not any(char.isupper() for char in password):
    print("Invalid password. Password must contain at least one uppercase character.")
elif not any(char.isdigit() for char in password):
    print("Invalid password. Password must contain at least one digit.")
else:
    print("Password is valid")
'''

# Task-6
'''
def transaction_list():
    for i in range(len(transactions)):
        print(i+1, transactions[i])

print("1. Withdrawal")
print("2. Deposit")
print("3. Exit")
    
transactions = []

while True:
    choice = int(input("Enter user's Choice: "))
    if choice == 1:
        withdraw = float(input('Enter withdrawal amount: '))
        transactions.append(f'Withdrawal : {withdraw}')
    elif choice == 2:
        deposit = float(input("Enter deposit amount: "))
        transactions.append(f'Deposit : {deposit}')
    elif choice == 3:
        transaction_list()
        print("Thank you for banking")
        break
    else:
        print("Invalid choice")
'''