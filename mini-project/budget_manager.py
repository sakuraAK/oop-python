from expense import Expense
from category import Category
from typing import Dict, List
import json

class BudgetManager:
    def __init__(self):
        self._categories: Dict[str, Category] = {}
        



    def add_category(self, name: str) -> bool:
        """
        Add new category
        
        :param self: Description
        :param name: Name of the expense catgory
        :type name: str
        :return: True if catgory added successfully. False - if exists
        :rtype: bool
        """
        if name in self._categories:
            return False
        self._categories[name] = Category(name)
        return True
    
    
    def remove_category(self, name: str) -> bool:
        if name in self._categories:
            del self._categories[name]
            return True
        
        return False
    
    def get_category(self, name: str) -> Category:
        return self._categories.get(name)
    
    
    def category_exists(self, name: str) -> bool:
        return name in self._categories
    
    
    def add_expense(self, category_name: str, expense: Expense) -> bool:
        if not category_name in self._categories:
            return False
        self._categories[category_name].add_expense(expense)
        return True
    
    def add_expense(self, category_name: str, description: str, amount: float, date: str=None) -> bool:
        if not category_name in self._categories:
            return False
    
        expense = Expense(description, amount, date)
        self._categories[category_name].add_expense(expense)
        return True
    
    def get_expenses_by_category(self, name: str) -> str:
        category = self.get_category(name)
        return category.list_expenses()
    
    def remove_expense(self, name: str, expense_id: int) -> bool:
        if not self.category_exists(name):
            print(f"Category {name} does not exist")
            return False
        
        category = self.get_category(name)
        
        return category.remove_expense(expense_id - 1)
    
    def list_categories(self) -> List[str]:
        return list(self._categories.keys())

    
    def get_all_categories(self) -> Dict[str, Category]:
        return self._categories.copy()
    
    
    def total_by_category(self) -> Dict[str, float]:
        return { name: category.total_amount() for name, category in self._categories.items() }
    
    def overall_total(self) -> float:
        return sum(category.total_amount() for category in self._categories.values())
    
    
    def __str__(self):
        if not self._categories:
            return "No categories yet"
    
        result = "Budget overview:\n"
        for category in self._categories.values():
            result += f"    {category}\n"
        result += f"\nOverall Total: ${self.overall_total():.2f}"
        
        return result 
            
    
    def to_dict(self) -> dict:
        return { "categories": { name: category.to_dict() for name, category in self._categories.items()} }
    
    
    @classmethod
    def from_dict(cls, data) -> "BudgetManager":
        budget_manager = cls()
        for category_data in data.get("categories", {}).values():
            budget_manager._categories[category_data["name"]] = Category.from_dict(category_data)
        return budget_manager
    
    def save_to_file(self, filename) -> bool:
        try:
            with open(filename, "w") as f:
                json.dump(self.to_dict(), f, indent=2)
                return True
        except IOError as e:
            print(f"Error saving file: {e}")
            return False
    
    def load_from_file(self, filename) -> bool:
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            loaded_manager = BudgetManager.from_dict(data)
            self._categories = loaded_manager.get_all_categories()
            return True
        except FileNotFoundError:
            print(f"File {filename} not found")
            return False
        except json.JSONDecodeError as e:
            print(f"Could not decode JSON: {e}")
            return False
        except IOError as e:
            print(f"Could not open file: {filename}")
            return False
            
                
    