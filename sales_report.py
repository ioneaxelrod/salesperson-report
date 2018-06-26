"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""


def print_sales_report(file_path):
    """
    Prints sales report showing total number of melon each salesperson sold
    :param file_path: string representing relative file path to file being read
    :return: None, prints output to console
    """

    # Create an empty dictionary
    employee_sales = {}

    # Opening file safely
    with open(file_path) as f:
        for line in f:

            # Converting line into sales data
            line = line.rstrip()
            entries = line.split("|")
            salesperson = entries[0]
            melons = int(entries[2])

            # Checking if data is already in dictionary, so any existing data is not overwritten
            if salesperson in employee_sales:
                employee_sales[salesperson] += melons
            else:
                employee_sales[salesperson] = melons

    # Iterating through each employee and sales in the dictionary and printing the results
    for employee, sales in employee_sales.items():
        print(f"{employee} sold {sales} melons")



# Calling the function
print_sales_report("sales-report.txt")


