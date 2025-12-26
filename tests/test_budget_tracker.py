"""
Unit tests for the Personal Budget & Expense Tracker application.

Tests cover:
- Expense class creation, validation, and serialization
- Category class expense management and totals
- BudgetManager class category and file I/O operations
"""

import pytest
import json
import os
from pathlib import Path

# Import classes from mini-project
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "mini-project"))

from expense import Expense
from category import Category
from budget_manager import BudgetManager


class TestExpense:
    """Test cases for the Expense class."""

    def test_expense_creation(self):
        """Test creating an expense with valid data."""
        expense = Expense("Groceries", 50.00, "2025-12-19")
        assert expense.description == "Groceries"
        assert expense.amount == 50.00
        assert expense.date == "2025-12-19"

    def test_expense_creation_default_date(self):
        """Test creating an expense without specifying a date."""
        expense = Expense("Restaurant", 30.00)
        assert expense.description == "Restaurant"
        assert expense.amount == 30.00
        assert expense.date is not None  # Should have today's date

    def test_expense_invalid_amount_negative(self):
        """Test that negative amounts raise ValueError."""
        with pytest.raises(ValueError):
            Expense("Food", -50.00)

    def test_expense_invalid_amount_zero(self):
        """Test that zero amount raises ValueError."""
        with pytest.raises(ValueError):
            Expense("Food", 0)

    def test_expense_amount_property_setter(self):
        """Test setting amount through property with validation."""
        expense = Expense("Food", 30.00)
        expense.amount = 45.50
        assert expense.amount == 45.50

    def test_expense_amount_property_invalid(self):
        """Test setting invalid amount through property."""
        expense = Expense("Food", 30.00)
        with pytest.raises(ValueError):
            expense.amount = -10.00

    def test_expense_to_dict(self):
        """Test converting expense to dictionary."""
        expense = Expense("Groceries", 50.00, "2025-12-19")
        data = expense.to_dict()
        
        assert data["description"] == "Groceries"
        assert data["amount"] == 50.00
        assert data["date"] == "2025-12-19"

    def test_expense_from_dict(self):
        """Test creating expense from dictionary."""
        data = {
            "description": "Restaurant",
            "amount": 35.75,
            "date": "2025-12-18"
        }
        expense = Expense.from_dict(data)
        
        assert expense.description == "Restaurant"
        assert expense.amount == 35.75
        assert expense.date == "2025-12-18"

    def test_expense_serialization_roundtrip(self):
        """Test that expense can be serialized and deserialized."""
        original = Expense("Gas", 60.00, "2025-12-17")
        data = original.to_dict()
        restored = Expense.from_dict(data)
        
        assert original.description == restored.description
        assert original.amount == restored.amount
        assert original.date == restored.date

    def test_expense_string_representation(self):
        """Test string representation of expense."""
        expense = Expense("Coffee", 5.50, "2025-12-19")
        str_repr = str(expense)
        
        assert "Coffee" in str_repr
        assert "5.50" in str_repr
        assert "2025-12-19" in str_repr


class TestCategory:
    """Test cases for the Category class."""

    def test_category_creation(self):
        """Test creating a category."""
        category = Category("Food")
        assert category.name == "Food"
        assert category.get_expenses() == []

    def test_category_add_expense(self):
        """Test adding expense to category."""
        category = Category("Transport")
        expense = Expense("Gas", 50.00)
        
        category.add_expense(expense)
        
        assert len(category.get_expenses()) == 1
        assert category.get_expenses()[0] == expense

    def test_category_add_multiple_expenses(self):
        """Test adding multiple expenses to category."""
        category = Category("Food")
        exp1 = Expense("Groceries", 45.00)
        exp2 = Expense("Restaurant", 30.00)
        exp3 = Expense("Coffee", 5.50)
        
        category.add_expense(exp1)
        category.add_expense(exp2)
        category.add_expense(exp3)
        
        assert len(category.get_expenses()) == 3

    def test_category_total_amount(self):
        """Test calculating total spending in category."""
        category = Category("Food")
        category.add_expense(Expense("Groceries", 45.00))
        category.add_expense(Expense("Restaurant", 30.00))
        category.add_expense(Expense("Coffee", 5.50))
        
        assert category.total_amount() == pytest.approx(80.50)

    def test_category_total_amount_empty(self):
        """Test total amount for empty category."""
        category = Category("Transport")
        assert category.total_amount() == 0.0

    def test_category_remove_expense(self):
        """Test removing an expense from category."""
        category = Category("Food")
        exp1 = Expense("Groceries", 45.00)
        exp2 = Expense("Restaurant", 30.00)
        
        category.add_expense(exp1)
        category.add_expense(exp2)
        
        assert category.remove_expense(0)
        assert len(category.get_expenses()) == 1
        assert category.get_expenses()[0] == exp2

    def test_category_remove_expense_invalid_index(self):
        """Test removing expense with invalid index."""
        category = Category("Food")
        category.add_expense(Expense("Groceries", 45.00))
        
        assert not category.remove_expense(5)
        assert len(category.get_expenses()) == 1

    def test_category_to_dict(self):
        """Test converting category to dictionary."""
        category = Category("Food")
        category.add_expense(Expense("Groceries", 45.00, "2025-12-19"))
        category.add_expense(Expense("Restaurant", 30.00, "2025-12-18"))
        
        data = category.to_dict()
        
        assert data["name"] == "Food"
        assert len(data["expenses"]) == 2
        assert data["expenses"][0]["description"] == "Groceries"
        assert data["expenses"][1]["description"] == "Restaurant"

    def test_category_from_dict(self):
        """Test creating category from dictionary."""
        data = {
            "name": "Transport",
            "expenses": [
                {"description": "Gas", "amount": 50.00, "date": "2025-12-19"},
                {"description": "Taxi", "amount": 25.00, "date": "2025-12-18"}
            ]
        }
        category = Category.from_dict(data)
        
        assert category.name == "Transport"
        assert len(category.get_expenses()) == 2
        assert category.total_amount() == 75.00

    def test_category_serialization_roundtrip(self):
        """Test category serialization and deserialization."""
        original = Category("Food")
        original.add_expense(Expense("Groceries", 45.00, "2025-12-19"))
        original.add_expense(Expense("Restaurant", 30.00, "2025-12-18"))
        
        data = original.to_dict()
        restored = Category.from_dict(data)
        
        assert original.name == restored.name
        assert original.total_amount() == restored.total_amount()
        assert len(original.get_expenses()) == len(restored.get_expenses())

    def test_category_list_expenses(self):
        """Test listing expenses as formatted string."""
        category = Category("Food")
        category.add_expense(Expense("Groceries", 45.00))
        
        result = category.list_expenses()
        
        assert "Food" in result
        assert "Groceries" in result
        assert "45.00" in result

    def test_category_list_expenses_empty(self):
        """Test listing expenses when category is empty."""
        category = Category("Transport")
        result = category.list_expenses()
        
        assert "No expenses" in result


class TestBudgetManager:
    """Test cases for the BudgetManager class."""

    def test_budget_manager_creation(self):
        """Test creating a budget manager."""
        manager = BudgetManager()
        assert manager.list_categories() == []

    def test_add_category(self):
        """Test adding a category."""
        manager = BudgetManager()
        assert manager.add_category("Food")
        assert "Food" in manager.list_categories()

    def test_add_duplicate_category(self):
        """Test that duplicate categories are not added."""
        manager = BudgetManager()
        manager.add_category("Food")
        assert not manager.add_category("Food")

    def test_remove_category(self):
        """Test removing a category."""
        manager = BudgetManager()
        manager.add_category("Food")
        
        assert manager.remove_category("Food")
        assert "Food" not in manager.list_categories()

    def test_remove_nonexistent_category(self):
        """Test removing a category that doesn't exist."""
        manager = BudgetManager()
        assert not manager.remove_category("Food")

    def test_category_exists(self):
        """Test checking if category exists."""
        manager = BudgetManager()
        manager.add_category("Food")
        
        assert manager.category_exists("Food")
        assert not manager.category_exists("Transport")

    def test_get_category(self):
        """Test getting a category by name."""
        manager = BudgetManager()
        manager.add_category("Food")
        
        category = manager.get_category("Food")
        
        assert category is not None
        assert category.name == "Food"

    def test_get_nonexistent_category(self):
        """Test getting a nonexistent category returns None."""
        manager = BudgetManager()
        assert manager.get_category("Food") is None

    def test_add_expense(self):
        """Test adding expense to category."""
        manager = BudgetManager()
        manager.add_category("Food")
        expense = Expense("Groceries", 45.00)
        
        assert manager.add_expense("Food", expense)
        
        category = manager.get_category("Food")
        assert len(category.get_expenses()) == 1

    def test_add_expense_to_nonexistent_category(self):
        """Test adding expense to nonexistent category."""
        manager = BudgetManager()
        expense = Expense("Groceries", 45.00)
        
        assert not manager.add_expense("Food", expense)

    def test_total_by_category(self):
        """Test getting totals by category."""
        manager = BudgetManager()
        manager.add_category("Food")
        manager.add_category("Transport")
        
        manager.add_expense("Food", Expense("Groceries", 45.00))
        manager.add_expense("Food", Expense("Restaurant", 30.00))
        manager.add_expense("Transport", Expense("Gas", 50.00))
        
        totals = manager.total_by_category()
        
        assert totals["Food"] == pytest.approx(75.00)
        assert totals["Transport"] == pytest.approx(50.00)

    def test_overall_total(self):
        """Test calculating overall total spending."""
        manager = BudgetManager()
        manager.add_category("Food")
        manager.add_category("Transport")
        
        manager.add_expense("Food", Expense("Groceries", 45.00))
        manager.add_expense("Food", Expense("Restaurant", 30.00))
        manager.add_expense("Transport", Expense("Gas", 50.00))
        
        assert manager.overall_total() == pytest.approx(125.00)

    def test_overall_total_empty(self):
        """Test overall total for empty budget."""
        manager = BudgetManager()
        assert manager.overall_total() == 0.0

    def test_budget_manager_to_dict(self):
        """Test converting budget to dictionary."""
        manager = BudgetManager()
        manager.add_category("Food")
        manager.add_expense("Food", Expense("Groceries", 45.00, "2025-12-19"))
        
        data = manager.to_dict()
        
        assert "categories" in data
        assert "Food" in data["categories"]
        assert len(data["categories"]["Food"]["expenses"]) == 1

    def test_budget_manager_from_dict(self):
        """Test creating budget manager from dictionary."""
        data = {
            "categories": {
                "Food": {
                    "name": "Food",
                    "expenses": [
                        {"description": "Groceries", "amount": 45.00, "date": "2025-12-19"}
                    ]
                }
            }
        }
        manager = BudgetManager.from_dict(data)
        
        assert "Food" in manager.list_categories()
        assert manager.overall_total() == 45.00

    def test_budget_manager_serialization_roundtrip(self):
        """Test budget manager serialization and deserialization."""
        original = BudgetManager()
        original.add_category("Food")
        original.add_category("Transport")
        original.add_expense("Food", Expense("Groceries", 45.00))
        original.add_expense("Transport", Expense("Gas", 50.00))
        
        data = original.to_dict()
        restored = BudgetManager.from_dict(data)
        
        assert original.overall_total() == restored.overall_total()
        assert set(original.list_categories()) == set(restored.list_categories())

    def test_save_and_load_file(self, tmp_path):
        """Test saving to and loading from file."""
        # Create and save budget
        manager = BudgetManager()
        manager.add_category("Food")
        manager.add_category("Transport")
        manager.add_expense("Food", Expense("Groceries", 45.00, "2025-12-19"))
        manager.add_expense("Transport", Expense("Gas", 50.00, "2025-12-19"))
        
        # Save to temporary file
        temp_file = tmp_path / "budget.json"
        assert manager.save_to_file(str(temp_file))
        assert temp_file.exists()
        
        # Load into new manager
        new_manager = BudgetManager()
        assert new_manager.load_from_file(str(temp_file))
        
        # Verify data matches
        assert new_manager.overall_total() == manager.overall_total()
        assert set(new_manager.list_categories()) == set(manager.list_categories())

    def test_save_creates_valid_json(self, tmp_path):
        """Test that saved file contains valid JSON."""
        manager = BudgetManager()
        manager.add_category("Food")
        manager.add_expense("Food", Expense("Groceries", 45.00))
        
        temp_file = tmp_path / "budget.json"
        manager.save_to_file(str(temp_file))
        
        # Verify file contains valid JSON
        with open(temp_file, "r") as f:
            data = json.load(f)
        
        assert "categories" in data
        assert isinstance(data, dict)

    def test_load_nonexistent_file(self):
        """Test loading from nonexistent file."""
        manager = BudgetManager()
        assert not manager.load_from_file("nonexistent_file.json")

    def test_load_invalid_json(self, tmp_path):
        """Test loading from file with invalid JSON."""
        temp_file = tmp_path / "invalid.json"
        temp_file.write_text("This is not valid JSON {")
        
        manager = BudgetManager()
        assert not manager.load_from_file(str(temp_file))

    def test_get_all_categories(self):
        """Test getting all categories as dictionary."""
        manager = BudgetManager()
        manager.add_category("Food")
        manager.add_category("Transport")
        
        categories = manager.get_all_categories()
        
        assert len(categories) == 2
        assert "Food" in categories
        assert "Transport" in categories


class TestIntegration:
    """Integration tests for complete workflows."""

    def test_complete_workflow(self, tmp_path):
        """Test a complete workflow from creation to save and load."""
        # Create budget and add data
        manager = BudgetManager()
        manager.add_category("Food")
        manager.add_category("Transport")
        manager.add_category("Entertainment")
        
        manager.add_expense("Food", Expense("Groceries", 45.00, "2025-12-19"))
        manager.add_expense("Food", Expense("Restaurant", 35.50, "2025-12-18"))
        manager.add_expense("Transport", Expense("Gas", 50.00, "2025-12-17"))
        manager.add_expense("Entertainment", Expense("Movie", 15.00, "2025-12-16"))
        
        # Verify totals
        assert manager.overall_total() == pytest.approx(145.50)
        assert manager.total_by_category()["Food"] == pytest.approx(80.50)
        
        # Save to file
        temp_file = tmp_path / "budget.json"
        assert manager.save_to_file(str(temp_file))
        
        # Load from file
        new_manager = BudgetManager()
        assert new_manager.load_from_file(str(temp_file))
        
        # Verify everything matches
        assert new_manager.overall_total() == pytest.approx(145.50)
        assert len(new_manager.list_categories()) == 3
        assert new_manager.total_by_category()["Food"] == pytest.approx(80.50)

    def test_multiple_save_load_cycles(self, tmp_path):
        """Test multiple save and load cycles maintain data integrity."""
        temp_file = tmp_path / "budget.json"
        
        # First cycle
        manager1 = BudgetManager()
        manager1.add_category("Food")
        manager1.add_expense("Food", Expense("Groceries", 45.00))
        manager1.save_to_file(str(temp_file))
        
        # Second cycle
        manager2 = BudgetManager()
        manager2.load_from_file(str(temp_file))
        manager2.add_expense("Food", Expense("Restaurant", 30.00))
        manager2.save_to_file(str(temp_file))
        
        # Third cycle
        manager3 = BudgetManager()
        manager3.load_from_file(str(temp_file))
        
        assert manager3.overall_total() == pytest.approx(75.00)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
