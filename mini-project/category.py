from expense import Expense
from typing import List

"""
"""

class Category:
    """
    Docstring for Category
    """
    def __init__(self, name):
        self.name = name
        self._expenses: List[Expense] = []
    
    
    def add_expense(self, expense: Expense) -> None:
        self._expenses.append(expense)
        
    
    def remove_expense(self, idx: int) -> bool:
        if 0 <= idx < len(self._expenses):
            self._expenses.pop(idx)
            return True
        return False
    
    def get_expenses(self) -> List[Expense]:
        return self._expenses.copy()


    def total_amount(self) -> float:
        return sum(expense.amount for expense in self._expenses)
    
    
    def list_expenses(self) -> str:
        
        if not self._expenses:
            return f"   No expenses in category: {self.name}"
        
        result = f"\n   Expenses in {self.name}:"
        for i, expense in enumerate(self._expenses, 1):
            result += f"\n  {i}. {expense}"
        return result
    
    def __str__(self):
        return f"{self.name} ({self.total_amount:.2f}) - {len(self._expenses)} expenses"
    
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "expenses": [expense.to_dict() for expense in self._expenses]
        }
        
    
    @classmethod
    def from_dict(cls, data) -> "Category":
        category = cls(name=data["name"])
        for expense_dict in data.get("expenses", []):
            category.add_expense(Expense.from_dict(expense_dict))
        
        return category