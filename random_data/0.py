import random
import datetime
import csv

def generate_random_data(num_records):
    data = []
    for _ in range(num_records):
        date = datetime.datetime(random.randint(2023, 2024), random.randint(1, 12), random.randint(1, 28)).strftime('%d-%m-%Y')
        category = random.choice(["Income", "Expense"])
        amount = random.randint(100, 1000)
        payment_method = random.choice(["Cash", "Bkash", "Nagad", "Credit Card"])
        description = f"{random.choice(['Salary', 'Rent', 'Groceries', 'Shopping', 'Transfer'])} "
        data.append([date, category, amount, payment_method, description])
    return data

# Get user input for the number of records
num_records = int(input("Enter the number of records to generate: "))

# Generate random data points
data = generate_random_data(num_records)

# Write data to CSV
with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Date', 'Category', 'Amount', 'Payment Method', 'Description']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    writer.writerows(data)

print(f"{num_records} records have been generated and saved to data.csv.")
