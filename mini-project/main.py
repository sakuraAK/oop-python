from budget_manager  import BudgetManager



def dislay_menu():
    print("Budget tracker menu options:")
    print("1. Add category")
    print("2. Add expense")
    print("3. View expenses in category")
    print("4. View total per category")
    print("5. View overall total")
    print("6. Remove expense")
    print("7. Save data")
    print("8. Load data")
    print("0. Exit")
    

def add_category(manager: BudgetManager):
    name = input("\nEnter category name: ").strip()
    if not manager.add_category(name):
        raise ValueError(f"Category {name} already exists")
    print(f"\nCategory {name} was added")

def add_expense(manager: BudgetManager):
    
    chosen_category = get_category(manager)
    
    description = input("\nProvide description: ").strip()
    amount = float(input("\nProvide amount: ").strip())
    date = input("\nProvide date(YYYY-MM-DD): ").strip()
    if manager.add_expense(chosen_category, description, amount, date):
        print("Expense added successfully")
    else:
        print("Could no add expense")
    
    
def get_category(manager: BudgetManager) -> str:
    print("\nAvailable catgories:\n")
    
    categories = manager.list_categories()
    for category in categories:
        print(f"1. {category}\n")
    
    idx = int(input("\nEnter catgory number: ").strip()) - 1
    if idx < 0 or idx >= len(categories):
        raise ValueError("Invalid categroy selected")
    chosen_category = categories[idx]
    return chosen_category

def view_expenses(manager: BudgetManager):
    category = get_category(manager)
    print(manager.get_expenses_by_category(category))
    
def view_total_per_category(manager: BudgetManager):
    result = manager.total_by_category()
    if not result:
        print("\nNo expenses yet")
        return

    print("\nTotal amounts per category:\n")
    for category, amount in result.items():
        print(f"{category}: {amount:.2f}\n")
    
def view_total(manager: BudgetManager):
    total_amount = manager.overall_total()
    print(f"\nTotal expenses: {total_amount:.2f}\n")

def remove_expense(manager:BudgetManager):
    category  = get_category(manager)
    print(f"\nList of expenses for {category}:\n")
    print(manager.get_expenses_by_category(category))
    expense_id = int(input("\nEnter the number of expense to remove: ").strip())
    if manager.remove_expense(category, expense_id):
        print("\nExpense successfully removed")
    else: 
        print("\nCould not remove the expense")

def save_to_file(manager: BudgetManager):
    file_name = input("\nEnter file name, default data.json: ").strip()
    if not file_name:
        file_name = "data.json" 
    if manager.save_to_file(file_name):
        print(f"\nSaved successfully to {file_name}")
    else:
        print(f"\nCould not save to {file_name}")    

def load_from_file(manager: BudgetManager):
    file_name = input("\nEnter file name, default data.json: ").strip()
    if not file_name:
        file_name = "data.json" 
    if manager.load_from_file(file_name):
        print(f"\n Data successfully loaded from {file_name}")
    else:
        print(f"\nCould not load the date from {file_name}")    

def main():
    print("Welcome to Budget Tracking Application")
    print("=" * 50)
    manager = BudgetManager()
    while True:
        dislay_menu()
        choice = input("Enter your choice (0-9): ").strip()
        try:
            if choice == "1":
                add_category(manager)
            elif choice == "2":
                add_expense(manager)
            elif choice == "3":
                view_expenses(manager)
            elif choice == "4":
                view_total_per_category(manager)
            elif choice == "5":
                view_total(manager)
            elif choice == "6":
                remove_expense(manager)
            elif choice == "7":
                save_to_file(manager)
            elif choice == "8":
                load_from_file(manager)
            elif choice == "0":
                print("\nGoodbye\n")
                break
            else:
               raise ValueError("Invalid option")
        except ValueError as e:
            print(e)
        
          



if __name__ == "__main__":
    main()
    
    