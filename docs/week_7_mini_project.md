Below is a **mini-project** to cover **all material from Week 1 → Week 7**, including:

- ✔ Classes & Objects
- ✔ Encapsulation
- ✔ Inheritance
- ✔ Composition & Relationships
- ✔ Collections of objects
- ✔ File I/O
- ✔ JSON serialization
- ✔ Application structure + workflow

---

# ⭐ **Mini-Project: Personal Budget & Expense Tracker (Console App)**

A small system that allows users to track categories (e.g., Food, Transport) and store many Expense objects.
All data is saved/loaded as JSON.

This project covers everything studied so far.

---

# **🎯 Learning Outcomes (What It Covers)**

| Week | Topic                       | Covered in Mini-Project                              |
| ---- | --------------------------- | ---------------------------------------------------- |
| 1    | Classes, objects            | Expense, Category, BudgetManager classes             |
| 2    | Encapsulation               | Private attributes (e.g., `_amount`) with validation |
| 3    | `__init__`, attributes      | All classes implemented                              |
| 4    | Inheritance basics          | Optional bonus: different expense types              |
| 5    | Composition & relationships | Categories contain expenses (aggregation)            |
| 6    | Abstract classes/interfaces | Optional: abstract base Expense class                |
| 7    | Collections & JSON/File I/O | Save/load expenses & categories                      |

---

# 📌 **Project Summary**

You will build:

1. **Expense class**
2. **Category class**, which aggregates multiple Expense objects
3. **BudgetManager class** to manage collections of categories
4. **JSON file I/O** to save and load data
5. A simple **console menu** for interacting with the system

---

# 📐 **PROJECT STRUCTURE (Simple Version)**

```
BudgetManager
 ├── 1..* Category
 │ └── 0..* Expense
```

- BudgetManager manages many categories
- Each category contains many expenses
- The app saves/loads everything through JSON

---

# 🧱 **Step-by-Step Plan**

---

# **STEP 1 — Create the Expense class (Week 1–2 concepts)**

Attributes:

- `description`
- `amount`
- `date`

Skills covered:

- constructors
- simple objects
- encapsulation (`_amount`)
- property with validation

Methods:

- `to_dict()`
- `from_dict()` (class method)

---

# **STEP 2 — Create the Category class (Aggregation)**

Each Category contains a list of expenses.

Attributes:

- `name`
- `_expenses` (list of Expense objects)

Methods:

- `add_expense(expense)`
- `total_amount()`
- `list_expenses()`
- `to_dict()` (convert expenses to dicts)
- `from_dict()`

Skills covered:

- aggregation
- managing many objects in a list
- composition-like behavior
- using loops, list operations

---

# **STEP 3 — Create BudgetManager (Managing collections of objects)**

BudgetManager manages a dictionary of categories.

Attributes:

- `_categories` — dict: `"Food" → Category`

Methods:

- `add_category(name)`
- `add_expense(category_name, expense)`
- `list_categories()`
- `overall_total()`
- `to_dict()` (all categories)
- `from_dict()`

Skills covered:

- dictionaries storing objects
- nested structures
- iteration

---

# **STEP 4 — JSON File I/O (Week 7)**

Add:

- `save_to_file(filename)`
- `load_from_file(filename)`

Steps:

1. Convert everything to a dict via `to_dict()`
2. Use `json.dump` and `json.load`
3. Convert dictionaries back into objects

Skills covered:

- JSON serializing nested objects
- File reading/writing
- Rebuilding objects from data

---

# **STEP 5 — Console UI (Optional but recommended)**

Create a simple text menu:

```
1. Add category
2. Add expense
3. View expenses in category
4. View total per category
5. View overall total
6. Save data
7. Load data
0. Exit
```

Skills covered:

- control flow
- input handling
- application structure

---

# **STEP 6 — Optional Inheritance Layer (Week 4/6)**

(Not required, but great extension.)

Create specialized expense types:

- FoodExpense
- TransportExpense
- OnlinePurchaseExpense

Add:

- an abstract base class `BaseExpense` with `@abstractmethod to_dict()`

This showcases:

- inheritance
- abstract classes/interfaces
- polymorphic collections

---

# **STEP 7 — Testing the Project Manually**

Try:

- creating 3 categories
- adding 4–10 expenses
- saving
- restarting the program
- loading the saved JSON
- verifying totals match

---

# **📄 Deliverables for Students**

Your students should produce:

1. `expense.py`
2. `category.py`
3. `budget_manager.py`
4. `main.py` with menu loop
5. `data.json`
6. README.md describing the program

---

# ⭐ Optional Enhancements for Advanced Students

- Add CSV export
- Add monthly summaries
- Add Expense ID system
- Add date validation
- Add editing/deleting expenses
- Add setting monthly budget limits
- Add color-coded console UI
- Add input error handling
