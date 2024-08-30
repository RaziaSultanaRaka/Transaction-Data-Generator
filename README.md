# Transaction Data Generator

## Description

The **Transaction Data Generator** is a Python script that generates random financial transaction data and saves it to a CSV file. This script can be useful for testing, simulations, or creating sample datasets for financial analysis or personal finance tracking applications.

## Features

- **Random Date Generation**: Generates random transaction dates within a specified range (2023-2024).
- **Category Assignment**: Assigns each transaction to either "Income" or "Expense."
- **Random Amounts**: Generates random transaction amounts between 100 and 1000 units.
- **Payment Methods**: Randomly selects a payment method from options like "Cash," "Bkash," "Nagad," and "Credit Card."
- **Customizable Descriptions**: Provides a random description for each transaction, such as "Salary," "Rent," "Groceries," "Shopping," or "Transfer."
- **User Input**: Allows users to specify the number of records they want to generate.

## How to Use

1. **Prerequisites**: Ensure you have Python installed on your system.

2. **Running the Script**:
    - Clone or download the script to your local machine.
    - Open a terminal or command prompt.
    - Navigate to the directory containing the script.
    - Run the script using the command: `python 0.py`
    - Enter the number of records you wish to generate when prompted.

3. **Output**:
    - The script will generate the specified number of transaction records and save them to a file named `data.csv` in the same directory.

## Customization

The script can be easily modified to:

- Change the range of random dates.
- Adjust the range of transaction amounts.
- Add or modify the list of categories, payment methods, and descriptions.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
