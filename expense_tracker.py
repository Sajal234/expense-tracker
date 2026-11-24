"""Personal Expense Tracker - UCS 745 Cloud and DevOps Lab Assignment Q1"""
expenses = []
def add_expense(item, amount):
    expenses.append((item, amount))
    return f"Added: {item} - Rs.{amount}"
def total_expense():
    return sum(amount for _, amount in expenses)
def show_title():
    return "Track Every Rupee - Daily Kharcha Manager: Smart & Easy Expense Tracker"

if __name__ == "__main__":
    print(show_title())
    print(add_expense("Notebook", 120))
    print(add_expense("Pen", 30))
    print(add_expense("Snacks", 80))
    print("Total Expense =", total_expense())
