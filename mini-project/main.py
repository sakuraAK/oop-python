"""
Console-based Personal Budget & Expense Tracker application.
"""

from budget_manager import BudgetManager
from expense import Expense


def display_menu() -> None:
    """Display the main menu options."""
    print("\n" + "=" * 50)
    print("Personal Budget & Expense Tracker")
    print("=" * 50)
    print("1. Add a new category")
    print("2. Add an expense to a category")
    print("3. View expenses in a category")
    print("4. View total per category")
    print("5. View overall total")
    print("6. Remove an expense")
    print("7. Save data")
    print("8. Load data")
    print("9. List all categories")
    print("0. Exit")
    print("=" * 50)


def add_category(manager: BudgetManager) -> None:
    """Add a new category to the budget."""
    name = input("Enter category name: ").strip()
    if not name:
        print("Category name cannot be empty.")
        return
    
    if manager.add_category(name):
        print(f"Category '{name}' added successfully.")
    else:
        print(f"Category '{name}' already exists.")


def add_expense(manager: BudgetManager) -> None:
    """Add an expense to a category."""
    categories = manager.list_categories()
    
    if not categories:
        print("No categories available. Please create one first.")
        return
    
    print("\nAvailable categories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")
    
    try:
        choice = int(input("Select category (enter number): "))
        if 1 <= choice <= len(categories):
            category_name = categories[choice - 1]
        else:
            print("Invalid selection.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    description = input("Enter expense description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid number for amount.")
        return
    
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    
    try:
        expense = Expense(description, amount, date if date else None)
        if manager.add_expense(category_name, expense):
            print(f"Expense added to '{category_name}'.")
        else:
            print("Failed to add expense.")
    except ValueError as e:
        print(f"Error: {e}")


def view_expenses(manager: BudgetManager) -> None:
    """View all expenses in a category."""
    categories = manager.list_categories()
    
    if not categories:
        print("No categories available.")
        return
    
    print("\nAvailable categories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")
    
    try:
        choice = int(input("Select category (enter number): "))
        if 1 <= choice <= len(categories):
            category_name = categories[choice - 1]
        else:
            print("Invalid selection.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    category = manager.get_category(category_name)
    print(category.list_expenses())


def view_totals(manager: BudgetManager) -> None:
    """View total spending per category."""
    totals = manager.total_by_category()
    
    if not totals:
        print("No categories available.")
        return
    
    print("\n" + "-" * 40)
    print("Total per Category:")
    print("-" * 40)
    for category_name, total in totals.items():
        print(f"  {category_name}: ${total:.2f}")
    print("-" * 40)


def view_overall_total(manager: BudgetManager) -> None:
    """View overall spending across all categories."""
    total = manager.overall_total()
    print("\n" + "=" * 40)
    print(f"Overall Total Spending: ${total:.2f}")
    print("=" * 40)


def remove_expense(manager: BudgetManager) -> None:
    """Remove an expense from a category."""
    categories = manager.list_categories()
    
    if not categories:
        print("No categories available.")
        return
    
    print("\nAvailable categories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")
    
    try:
        choice = int(input("Select category (enter number): "))
        if 1 <= choice <= len(categories):
            category_name = categories[choice - 1]
        else:
            print("Invalid selection.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    category = manager.get_category(category_name)
    expenses = category.get_expenses()
    
    if not expenses:
        print(f"No expenses in '{category_name}'.")
        return
    
    print(f"\nExpenses in {category_name}:")
    for i, expense in enumerate(expenses, 1):
        print(f"  {i}. {expense}")
    
    try:
        exp_choice = int(input("Select expense to remove (enter number): "))
        if category.remove_expense(exp_choice - 1):
            print("✓ Expense removed successfully.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")


def save_data(manager: BudgetManager) -> None:
    """Save budget data to file."""
    filename = input("Enter filename (default: budget_data.json): ").strip()
    if not filename:
        filename = "budget_data.json"
    
    if manager.save_to_file(filename):
        print(f"✓ Data saved to '{filename}'.")
    else:
        print("Failed to save data.")


def load_data(manager: BudgetManager) -> None:
    """Load budget data from file."""
    filename = input("Enter filename (default: budget_data.json): ").strip()
    if not filename:
        filename = "budget_data.json"
    
    if manager.load_from_file(filename):
        print(f"✓ Data loaded from '{filename}'.")
    else:
        print("Failed to load data.")


def list_categories(manager: BudgetManager) -> None:
    """Display all categories."""
    categories = manager.list_categories()
    
    if not categories:
        print("No categories available.")
        return
    
    print("\n" + "-" * 40)
    print("All Categories:")
    print("-" * 40)
    for category in manager.get_all_categories().values():
        print(f"  {category}")
    print("-" * 40)


def main() -> None:
    """Main application loop."""
    manager = BudgetManager()
    
    print("\nWelcome to Personal Budget & Expense Tracker!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (0-9): ").strip()
        
        if choice == "1":
            add_category(manager)
        elif choice == "2":
            add_expense(manager)
        elif choice == "3":
            view_expenses(manager)
        elif choice == "4":
            view_totals(manager)
        elif choice == "5":
            view_overall_total(manager)
        elif choice == "6":
            remove_expense(manager)
        elif choice == "7":
            save_data(manager)
        elif choice == "8":
            load_data(manager)
        elif choice == "9":
            list_categories(manager)
        elif choice == "0":
            print("\nThank you for using the Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
