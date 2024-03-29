"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    total_months = int(input("How many months? "))

    monthly_income(incomes, total_months)

    print("\nIncome Report\n-------------")
    print_report(incomes, total_months)


def print_report(incomes, total_months):
    total = 0
    for month in range(1, total_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def monthly_income(incomes, total_months):
    for month in range(1, total_months + 1):
        income = float(input(f"Enter income for month {month}:"))
        incomes.append(income)


main()
